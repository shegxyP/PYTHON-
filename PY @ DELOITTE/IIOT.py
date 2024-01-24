import json
import unittest
import datetime

with open("./data-1.json", "r") as f:
  jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
  jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
  jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
  # IMPLEMENT: Conversion From Type 1
  converted_result = {
    "id": jsonObject["id"],
    "timestamp": datetime.datetime.utcfromtimestamp(jsonObject["timestamp"]),
    "data": {
      "temperature": jsonObject.get("temp"),
      "humidity": jsonObject.get("hum"),
      "pressure": jsonObject.get("press")
    }
  }
  return converted_result


def convertFromFormat2(jsonObject):
  # IMPLEMENT: Conversion From Type 2
  converted_result = {
    "id": jsonObject.get("deviceId"),
    "timestamp": datetime.datetime.utcfromtimestamp(jsonObject.get("time")),
    "data": {
      "temperature": jsonObject.get("sensors", {}).get("temp"),
      "humidity": jsonObject.get("sensors", {}).get("hum"),
      "pressure": jsonObject.get("sensors", {}).get("press")
    }
  }
  return converted_result


class TestSolution(unittest.TestCase):

  def test_sanity(self):
    self.assertEqual(convertFromFormat1(jsonData1), jsonExpectedResult,
                     'Converting from Type 1 failed')

  def test_dataType1(self):
    self.assertEqual(convertFromFormat2(jsonData2), jsonExpectedResult,
                     'Converting from Type 2 failed')

  def test_dataType2(self):
    self.assertEqual(jsonData1, jsonExpectedResult)


if __name__ == '__main__':
  unittest.main()
