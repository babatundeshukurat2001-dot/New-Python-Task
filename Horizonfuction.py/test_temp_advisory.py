# --- Tests ---
fron unittest import TestCase
import temp_advisory


def test_temp_advisory():
    assert temp_advisory(30, 'C', 90) == "Cold advisory"  
    assert temp_advisory(40, 'C', 100) == "Heat alert"    
    assert temp_advisory(32, 'F', 0) == "Heat alert"       
    assert temp_advisory(0, 'F', 0) == "Cold advisory"     
    print("All temp_advisory tests passed")

test_temp_advisory()
