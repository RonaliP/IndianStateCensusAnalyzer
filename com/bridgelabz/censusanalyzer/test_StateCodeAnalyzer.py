from com.bridgelabz.censusanalyzer.StateCodeCSVLoader import StateCodeCSVLoader
from com.bridgelabz.censusanalyzer.censusAnalyzerError import censusAnalyzererror
import pytest
csv_filepath= r"D:\PycharmProjects\CensusAnalyzer\IndiaStateCode.csv"
csv_wrongfilepath=r"C:\PycharmProjects\CensusAnalyzer\IndiaStateCode.csv"
CENSUS_CSV_FILE_WRONG_TYPE=r"D:\PycharmProjects\CensusAnalyzer\ModifiedCensus.csv"
CENSUS_CSV_FILE_WRONG_DELIMITER=r"D:\PycharmProjects\CensusAnalyzer\ModifiedCensus.csv"
def test_recordcount():
    csv_loader=StateCodeCSVLoader(csv_filepath)
    assert csv_loader.record_counter()== 37


def test_recordcount_wrongfilepath():
    csv_loader=StateCodeCSVLoader(csv_wrongfilepath)
    with pytest.raises(censusAnalyzererror):
        csv_loader.record_counter()

# Check if exception gets raised or not
def test_record_counter_for_wrong_file_type():
    csv_loader = StateCodeCSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(censusAnalyzererror):
        csv_loader.record_counter()


# Check if exception gets raised or not
# NOTE - Change delimiter of the file and save it
def test_record_counter_for_wrong_delimiter():
    csv_loader = StateCodeCSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(censusAnalyzererror):
        csv_loader.record_counter()




