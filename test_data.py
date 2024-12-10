from selenium.webdriver.common.by import By

config = {
    "username": "teacher",
    "password": "moodle2024"
}

const_path = {
    "save": "//button[contains(.,\'Save\')]",
    "show_more": "//a[contains(text(),\'Show more...\')]"
}

testcases = [
    {
      "id": "test_addEventByDefault",
      "field": "name",
      "inputName": "Event testing",
      "assertData": (By.XPATH, "//span[contains(.,\'Event testing\')]")
    },
        {
      "id": "test_addEventWithLocationAndDescription",
      "field": "locationanddescription",
      "inputName": "Event testing 1",
      "sendKeys": "Room 111",
      "assertData": (By.XPATH, "//span[contains(.,\'Event testing 1\')]")
    },
    {
      "id": "test_addEventWithoutTitle",
      "field": "name",
      "inputName": "",
      "assertData": (By.ID, "id_error_name", "- Required")
    },
    {
      "id": "test_addEventWithDuration",
      "field": "duration",
      "inputName": "Event testing 2",
      "assertData": (By.XPATH, "//span[contains(.,\'Event testing 2\')]")
    },
      {
      "id": "test_addEventWithRepetition",
      "field": "repeat",
      "inputName": "Event testing 3",
      "sendKeys": "3",
      "assertData": (By.XPATH, "//span[contains(.,\'Event testing 3\')]")
    }
]
