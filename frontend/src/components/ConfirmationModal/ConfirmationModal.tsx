import React from "react";
import {
  ModalBackdrop,
  ModalContent,
  ModalTitle,
  ModalText,
  ModalButtonRow,
} from "./ConfirmationModal.styles";
import Button from "../Button/Button";

export interface ConfirmationModalProps {
  onCancel: () => void;
  onConfirm: () => void;
}

const ConfirmationModal: React.FC<ConfirmationModalProps> = ({
  onCancel,
  onConfirm,
}) => {
  const handleContentClick = (e: React.MouseEvent) => {
    e.stopPropagation();
  };

  return (
    <ModalBackdrop onClick={onCancel}>
      <ModalContent onClick={handleContentClick}>
        <ModalTitle>Czy na pewno usunąć?</ModalTitle>
        <ModalText>
          Tej operacji nie można cofnąć. Wszystkie pytania w tym teście również
          zostaną usunięte.
        </ModalText>
        <ModalButtonRow>
          <Button variant="outline" onClick={onCancel}>
            Anuluj
          </Button>

          <Button variant="danger" onClick={onConfirm}>
            Usuń
          </Button>
        </ModalButtonRow>
      </ModalContent>
    </ModalBackdrop>
  );
};

export default ConfirmationModal;