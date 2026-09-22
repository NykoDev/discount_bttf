import pytest
from app.services.discount import Discount
from app.models.movie import Movie


@pytest.fixture
def sample_movies1():
    
    return [
        Movie(title='Back to the Future 1'),
        Movie(title='Back to the Future 3'),
    ]

@pytest.fixture
def sample_movies2():
    
    return [
        Movie(title='Back to the Future 1'),
        Movie(title='Back to the Future 2'),
        Movie(title='Back to the Future 3'),
        Movie(title='Back to the Future 2'),
    ]

@pytest.fixture
def sample_movies3():
    
    return [
        Movie(title='Back to the Future 1'),
        Movie(title='Back to the Future 2'),
        Movie(title='Back to the Future 3'),
        Movie(title='Other Movie'),
    ]

# Tests for the count_distinct_bttf_movies method
# Ensure detection of distinct BTTF movies is correct

def test_count_distinct_bttf_movies(sample_movies1):
    discount1 = Discount(sample_movies1)
    assert discount1.count_distinct_bttf_movies() == 2

def test_count_distinct_bttf_movies2(sample_movies2):       
    discount2 = Discount(sample_movies2)
    assert discount2.count_distinct_bttf_movies() == 3

def test_count_distinct_bttf_movies3(sample_movies3):       
    discount3 = Discount(sample_movies3)
    assert discount3.count_distinct_bttf_movies() == 3

# Test for the set_discount_price method
def test_set_discount_price():
    discount = Discount([])
    assert discount.set_discount_price(1) == 15
    assert discount.set_discount_price(2) == 13.5
    assert discount.set_discount_price(3) == 12.0

# test for the apply method
def test_apply_discount(sample_movies1):
    discount = Discount(sample_movies1)
    discount.apply()
    assert sample_movies1[0].price == 13.5  # 10% discount for 2 distinct BTTF movies
    assert sample_movies1[1].price == 13.5

def test_apply_discount2(sample_movies2):
    discount = Discount(sample_movies2)
    discount.apply()
    assert sample_movies2[0].price == 12.0  # 20% discount for 3 distinct BTTF movies
    assert sample_movies2[1].price == 12.0
    assert sample_movies2[2].price == 12.0
    assert sample_movies2[3].price == 12.0