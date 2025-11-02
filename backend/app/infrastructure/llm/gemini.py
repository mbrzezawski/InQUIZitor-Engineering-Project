from __future__ import annotations

import json
from functools import lru_cache
from typing import List

from google import genai

from app.api.schemas.tests import GenerateParams
from app.core.config import get_settings
from app.domain.models import Question
from app.domain.models.enums import QuestionDifficulty
from app.domain.services import QuestionGenerator


def _build_prompt(text: str, params: GenerateParams) -> str:
    parts = [
        "Pracujesz jako ekspert dydaktyczny języka polskiego.",
        "Twoim zadaniem jest przygotowanie pytań testowych na podstawie przekazanego materiału.",
        "Każde pytanie i wszystkie odpowiedzi muszą być w języku polskim.",
        f"Na podstawie poniższego tekstu utwórz {params.num_closed} pytań zamkniętych oraz {params.num_open} pytań otwartych.",
        f"\n\nTekst źródłowy:\n{text}\n",
    ]

    if params.closed_types:
        closed_types_str = ", ".join(params.closed_types)
        parts.append(
            f"Dla pytań zamkniętych korzystaj wyłącznie z następujących typów: {closed_types_str}."
        )

    parts.append(
        f"Rozłóż poziomy trudności następująco: {params.easy} łatwych, {params.medium} średnich, {params.hard} trudnych."
    )

    parts.append(
        """
        Zwróć każde pytanie jako obiekt JSON o strukturze:
        {
        "text": "...",  # treść pytania po polsku
        "is_closed": true | false,  # czy pytanie jest zamknięte
        "difficulty": 1 | 2 | 3,  # 1=łatwe, 2=średnie, 3=trudne
        "choices": [ ... ] lub null,  # lista wariantów odpowiedzi po polsku
        "correct_choices": [ ... ] lub null  # lista poprawnych odpowiedzi po polsku
        }
        Zwróć TYLKO tablicę JSON takich obiektów, bez komentarzy i dodatkowego tekstu.
        """
    )

    return "\n\n".join(parts)


class GeminiQuestionGenerator(QuestionGenerator):
    def __init__(self, model_name: str = "gemini-2.0-flash") -> None:
        self._model_name = model_name

    @staticmethod
    @lru_cache()
    def _client() -> genai.Client:
        settings = get_settings()
        return genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate(self, *, source_text: str, params: GenerateParams) -> List[Question]:
        prompt = _build_prompt(source_text, params)

        try:
            response = self._client().models.generate_content(
                model=self._model_name,
                contents=prompt,
            )
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(f"Gemini request failed: {exc}") from exc

        raw_output = response.text or ""
        if raw_output.startswith("```"):
            raw_output = raw_output.strip("`")
        if raw_output.startswith("json"):
            raw_output = raw_output[4:].strip()

        try:
            questions_payload = json.loads(raw_output)
        except json.JSONDecodeError as exc:  # noqa: B904
            raise ValueError(f"Failed to parse Gemini response as JSON:\n{raw_output}") from exc

        questions: List[Question] = []
        for item in questions_payload:
            missing = {"text", "is_closed", "difficulty", "choices", "correct_choices"} - item.keys()
            if missing:
                raise ValueError(f"Missing fields in the generated question: {missing}")

            difficulty = QuestionDifficulty(int(item["difficulty"]))
            choices = item["choices"] or []
            correct_choices = item["correct_choices"] or []

            question = Question(
                id=None,
                text=item["text"],
                is_closed=bool(item["is_closed"]),
                difficulty=difficulty,
                choices=choices,
                correct_choices=correct_choices,
            )
            questions.append(question)

        return questions


__all__ = ["GeminiQuestionGenerator"]

