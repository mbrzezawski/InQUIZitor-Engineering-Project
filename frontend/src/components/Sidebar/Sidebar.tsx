import React from "react";
import {
  SidebarWrapper,
  SearchInput,
  TestList,
  TestItem,
  CreateNewButton,
  DeleteIcon,
} from "./Sidebar.styles";

// 1. IMPORT YOUR TRASH ICON
import trashIcon from "../../assets/icons/trash.png"; 

export interface SidebarProps {
  tests: { id: number; title: string }[];
  onSelect: (testId: number) => void;
  onCreateNew: () => void;
  onDelete: (testId: number) => void;
}

const Sidebar: React.FC<SidebarProps> = ({
  tests,
  onSelect,
  onCreateNew,
  onDelete,
}) => {
  const handleDeleteClick = (
    e: React.MouseEvent<HTMLImageElement>,
    testId: number
  ) => {
    e.stopPropagation();
    onDelete(testId);
  };

  return (
    <SidebarWrapper>
      <SearchInput placeholder="Wyszukaj..." />
      <TestList>
        {tests.map((t) => (
          <TestItem key={t.id} onClick={() => onSelect(t.id)}>
            <span>{t.title}</span>
            <DeleteIcon
              src={trashIcon}
              alt="Delete"
              onClick={(e) => handleDeleteClick(e, t.id)}
            />
          </TestItem>
        ))}
      </TestList>
      <CreateNewButton onClick={onCreateNew}>
        + Utwórz nowy
      </CreateNewButton>
    </SidebarWrapper>
  );
};

export default Sidebar;