import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db


def test_createFruit_withValidData_createsFruitWithCorrectAttributes():
    """
    Test the creation of a Fruit instance with valid parameters.
    Verifies that the name and quantity of the fruit are set correctly.
    """
    fruit = Fruit(name="Apple", quantity=10)
    assert fruit.name == "Apple"
    assert fruit.quantity == 10


def test_calculateTotalFruits_withFruitsList_returnsCorrectFruitCount():
    """
    Test the calculation of the total number of fruits in an inventory.
    Checks if the total_fruits method returns the correct count.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Banana", quantity=5)]
    assert FruitMetrics.total_fruits(fruits) == 2


def test_calculateAverageQuantity_withFruitsList_returnsCorrectAverage():
    """
    Test the calculation of the average quantity of fruits in an inventory.
    Checks if the average_quantity method computes the correct average.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Banana", quantity=20)]
    assert FruitMetrics.average_quantity(fruits) == 15  # (10+20)/2


def test_identifyMostCommonFruit_withFruitsList_returnsMostFrequentFruit():
    """
    Test to identify the most common fruit in an inventory.
    Checks if the most_common_fruit method correctly identifies the fruit that appears most frequently.
    """
    fruits = [
        Fruit(name="Apple", quantity=10),
        Fruit(name="Banana", quantity=5),
        Fruit(name="Apple", quantity=2)
    ]
    assert FruitMetrics.most_common_fruit(fruits) == "Apple"


def test_createFruit_withValidDetails_createsFruitSuccessfully():
    """
    Test the creation of a valid Fruit instance.
    Verifies that a fruit with valid name and quantity is created without errors.
    """
    valid_fruit = Fruit(name="Apple", quantity=10)
    assert valid_fruit.name == "Apple"
    assert valid_fruit.quantity == 10


def test_createFruit_withInvalidName_raisesAssertionError():
    """
    Test the creation of a Fruit instance with an invalid name.
    Verifies that an AssertionError is raised when the name is empty.
    """
    with pytest.raises(AssertionError):
        Fruit(name="", quantity=10)


def test_createFruit_withNegativeQuantity_raisesAssertionError():
    """
    Test the creation of a Fruit instance with an invalid quantity.
    Verifies that an AssertionError is raised when the quantity is negative.
    """
    with pytest.raises(AssertionError):
        Fruit(name="Apple", quantity=-5)


def test_createFruit_withNonIntegerQuantity_raisesAssertionError():
    """
    Test the creation of a Fruit instance with an invalid quantity type.
    Verifies that an AssertionError is raised when the quantity is not an integer.
    """
    with pytest.raises(AssertionError):
        Fruit(name="Apple", quantity="ten")

def test_remove_fruit_by_name_removesCorrectFruit():
    """
    Test that remove_fruit_by_name removes the fruit with the specified name
    from the list and returns a new list.
    """
    fruits = [Fruit(name="Apple", quantity=10), Fruit(name="Banana", quantity=5)]
    new_fruits = FruitMetrics.remove_fruit_by_name(fruits, "Apple")
    
    assert len(new_fruits) == 1
    assert new_fruits[0].name == "Banana"
