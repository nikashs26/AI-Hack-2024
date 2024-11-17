import React, { useState } from 'react';

function DropdownMenu() {
`  const [isOpen, setIsOpen] = useState(false);

    const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown">
        <button className="dropdown-button" onClick={toggleDropdown}>
        Select an option
      </button>
      {isOpen && (
        <ul className="dropdown-menu">
    `  `<li>Option 1</li>
        <li>Option 2</li>
        <li>Option 3</li>
        </ul>
      )}
    </div>
  );
}

export default DropdownMenu;