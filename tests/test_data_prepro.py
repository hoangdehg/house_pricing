from data_prepro import prepro_data

def test_prepro_data():
    x = 10
    preprocessed_data = prepro_data(x)
    assert preprocessed_data == 11