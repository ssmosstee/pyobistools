"""
check eventDate
"""

import pandas as pd


data_nodate = pd.DataFrame({'scientificName': ["Abra alva", "Buccinum fusiforme", "Buccinum fusiforme", "Buccinum fusiforme", "ljkf hlqsdkf"]})

data_goodformats = pd.DataFrame({'eventDate': [ "2016", "2016-01", "2016-01-02", "2016-01-02 13:00", "2016-01-02T13:00", "2016-01-02 13:00:00/2016-01-02 14:00:00", "2016-01-02 13:00:00/14:00:00"]})

data_badformats = pd.DataFrame({'eventDate': ["2016/01/02", "2016-01-02 13h00"]})

"""
data_nodate <- data.frame(
  scientificName = c("Abra alba", "Lanice conchilega"),
  stringsAsFactors = FALSE
)

data_goodformats = pd.DataFrame({'scientificName': ["Abra alva", "Buccinum fusiforme", "Buccinum fusiforme", "Buccinum fusiforme", "ljkf hlqsdkf"]})
data_goodformats <- data.frame(
  eventDate = c(
    "2016",
    "2016-01",
    "2016-01-02",
    "2016-01-02 13:00",
    "2016-01-02T13:00",
    "2016-01-02 13:00:00/2016-01-02 14:00:00",
    "2016-01-02 13:00:00/14:00:00"
  ),
  stringsAsFactors = FALSE
)

data_badformats <- data.frame(
  eventDate = c(
    "2016/01/02",
    "2016-01-02 13h00"
  ),
  stringsAsFactors = FALSE
)
"""

def test_good_bad_eventdate():
    """
    good and bad eventDate work
    """
    assert 4 == 5

"""results <- check_eventdate(data_nodate)
  expect_equal(nrow(results), 1)

  results <- check_eventdate(data_goodformats)
  expect_equal(nrow(results), 0)

  results <- check_eventdate(data_badformats)
  expect_equal(nrow(results), nrow(data_badformats))
"""

def test_date_columns():
    """
    date columns are ok
    """
    assert 4 == 5

"""
  data <- data.frame(eventDate = c(as.Date("2006-01-12"), as.Date("2006-01-13"), NA))
  results <- check_eventdate(data)
  expect_equal(nrow(results), 1)
  expect_equal(results$row, 3)"""