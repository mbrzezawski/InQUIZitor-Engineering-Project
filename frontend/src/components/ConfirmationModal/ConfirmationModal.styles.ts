import styled from "styled-components";

export const ModalBackdrop = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 99;

  backdrop-filter: blur(5px);
  background-color: rgba(0, 0, 0, 0.4);

  display: flex;
  justify-content: center;
  align-items: center;
`;

export const ModalContent = styled.div`
  background-color: ${({ theme }) => theme.colors.neutral.white || "white"};
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  min-width: 320px;
  max-width: 600px;
  z-index: 100;
  display: flex;
  flex-direction: column;
  gap: 16px;
`;

export const ModalTitle = styled.h3`
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
`;

export const ModalText = styled.p`
  margin: 0;
  font-size: 1rem;
  color: ${({ theme }) => theme.colors.neutral.lGrey};
`;

export const ModalButtonRow = styled.div`
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 16px;
`;