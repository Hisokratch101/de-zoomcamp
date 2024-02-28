import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(name): 
    camel = name[0].lower()
    for i in range(1,len(name)):
        s = name[i]
        if s.isupper():
            s = "_"+ s.lower()
        camel += s
    return camel


@transformer
def transform(data, *args, **kwargs):
    #Remove null values from passenger_count
    data = data[data["passenger_count"]>0]
    data = data[data["trip_distance"]>0]
    #Create new column
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    
    data = data.rename(columns={"VendorID":"vendor_id","RatecodeID":"ratecode_id","PULocationID":"pulocation_id","DOLocationID":"dolocation_id"})

    return data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
