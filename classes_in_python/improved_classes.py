from datetime import date
from typing import List, Optional, Iterator, Generator


class Employee:
    """A class representing an employee with basic information and salary."""
    
    num_of_emps: int = 0
    raise_amount: float = 1.04
    
    def __init__(self, first: str, last: str, pay: int) -> None:
        """Initialize an employee with first name, last name, and pay.
        
        Args:
            first (str): First name of the employee
            last (str): Last name of the employee
            pay (int): Annual salary of the employee
        """
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1
        
    def fullname(self) -> str:
        """Return the full name of the employee."""
        return f"{self.first} {self.last}"
    
    def apply_raise(self) -> None:
        """Apply the raise amount to the employee's salary."""
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        """Set the raise amount for all employees.
        
        Args:
            amount (float): The new raise amount
        """
        if amount <= 0:
            raise ValueError("Raise amount must be positive")
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str: str) -> 'Employee':
        """Create an employee from a string in the format 'first-last-pay'.
        
        Args:
            emp_str (str): String in format 'first-last-pay'
            
        Returns:
            Employee: A new Employee instance
            
        Raises:
            ValueError: If the string format is invalid
        """
        try:
            first, last, pay = emp_str.split('-')
            return cls(first, last, int(pay))
        except (ValueError, TypeError):
            raise ValueError("Employee string must be in format 'first-last-pay'")
    
    @staticmethod
    def is_workday(day: date) -> bool:
        """Check if a given day is a workday.
        
        Args:
            day (date): The date to check
            
        Returns:
            bool: True if it's a workday, False otherwise
        """
        return day.weekday() < 5


class Developer(Employee):
    """A class representing a developer, inheriting from Employee."""
    
    raise_amount: float = 1.10  # Developers get a higher raise
    
    def __init__(self, first: str, last: str, pay: int, prog_lang: str) -> None:
        """Initialize a developer with programming language.
        
        Args:
            first (str): First name
            last (str): Last name
            pay (int): Annual salary
            prog_lang (str): Primary programming language
        """
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang.lower()  # Normalize programming language to lowercase


class Manager(Employee):
    """A class representing a manager, inheriting from Employee."""
    
    def __init__(self, first: str, last: str, pay: int, employees: Optional[List[Employee]] = None) -> None:
        """Initialize a manager with optional list of employees.
        
        Args:
            first (str): First name
            last (str): Last name
            pay (int): Annual salary
            employees (List[Employee], optional): List of employees managed by this manager
        """
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []
    
    def add_emp(self, emp: Employee) -> None:
        """Add an employee to the manager's team.
        
        Args:
            emp (Employee): Employee to add
            
        Raises:
            ValueError: If employee is already in the team
        """
        if emp in self.employees:
            raise ValueError(f"Employee {emp.fullname()} is already in the team")
        self.employees.append(emp)
    
    def remove_emp(self, emp: Employee) -> None:
        """Remove an employee from the manager's team.
        
        Args:
            emp (Employee): Employee to remove
            
        Raises:
            ValueError: If employee is not in the team
        """
        if emp not in self.employees:
            raise ValueError(f"Employee {emp.fullname()} is not in the team")
        self.employees.remove(emp)
    
    def print_emp(self) -> None:
        """Print the names of all employees in the manager's team."""
        for emp in self.employees:
            print(f"-> {emp.fullname()}")


class SquaresIterator:
    """An iterator class that generates square numbers up to a given maximum."""
    
    def __init__(self, max_root_value: int) -> None:
        """Initialize the iterator with a maximum root value.
        
        Args:
            max_root_value (int): Maximum value to square
        """
        if max_root_value < 0:
            raise ValueError("Maximum root value must be non-negative")
        self.max_root_value = max_root_value
        self.current_root_value = 0
    
    def __iter__(self) -> Iterator[int]:
        """Return the iterator object itself."""
        return self
    
    def __next__(self) -> int:
        """Return the next square number in the sequence.
        
        Returns:
            int: The next square number
            
        Raises:
            StopIteration: When all squares have been generated
        """
        if self.current_root_value >= self.max_root_value:
            raise StopIteration
        square_value = self.current_root_value ** 2
        self.current_root_value += 1
        return square_value


def make_squares(n: int) -> Generator[int, None, None]:
    """Generate square numbers up to n-1.
    
    Args:
        n (int): Maximum value to square
        
    Yields:
        int: Square numbers from 0 to (n-1)^2
    """
    for i in range(n):
        yield i ** 2 