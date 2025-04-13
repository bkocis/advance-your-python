from datetime import date
from improved_classes import Employee, Developer, Manager, SquaresIterator, make_squares


def test_employee():
    """Test the Employee class functionality."""
    # Create an employee
    emp = Employee("John", "Doe", 50000)
    print(f"Employee: {emp.fullname()}, Salary: ${emp.pay}")
    
    # Apply raise
    emp.apply_raise()
    print(f"After raise: ${emp.pay}")
    
    # Create from string
    emp2 = Employee.from_string("Jane-Smith-60000")
    print(f"Employee from string: {emp2.fullname()}, Salary: ${emp2.pay}")
    
    # Check workday
    today = date.today()
    print(f"Is today a workday? {Employee.is_workday(today)}")


def test_developer():
    """Test the Developer class functionality."""
    # Create a developer
    dev = Developer("Alice", "Johnson", 70000, "Python")
    print(f"Developer: {dev.fullname()}, Language: {dev.prog_lang}")
    
    # Apply developer raise
    dev.apply_raise()
    print(f"After developer raise: ${dev.pay}")


def test_manager():
    """Test the Manager class functionality."""
    # Create employees
    emp1 = Employee("Bob", "Wilson", 50000)
    emp2 = Employee("Carol", "Davis", 55000)
    
    # Create manager with employees
    manager = Manager("Eve", "Brown", 80000, [emp1, emp2])
    print(f"Manager: {manager.fullname()}")
    print("Team members:")
    manager.print_emp()
    
    # Add new employee
    emp3 = Employee("Dave", "Miller", 52000)
    manager.add_emp(emp3)
    print("\nAfter adding new employee:")
    manager.print_emp()
    
    # Try to add duplicate employee
    try:
        manager.add_emp(emp3)
    except ValueError as e:
        print(f"\nError when adding duplicate: {e}")


def test_iterators():
    """Test the iterator functionality."""
    # Using SquaresIterator
    print("Using SquaresIterator:")
    for num in SquaresIterator(5):
        print(num)
    
    # Using generator function
    print("\nUsing make_squares generator:")
    for num in make_squares(5):
        print(num)


if __name__ == "__main__":
    print("=== Testing Employee Class ===")
    test_employee()
    
    print("\n=== Testing Developer Class ===")
    test_developer()
    
    print("\n=== Testing Manager Class ===")
    test_manager()
    
    print("\n=== Testing Iterators ===")
    test_iterators() 