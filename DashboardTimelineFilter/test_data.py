from selenium.webdriver.common.by import By

config = {
    "username": "teacher",
    "password": "moodle2024"
}

testcases = [
    # {
    #   "id": "test_allDeadlineSortByDate",
    #   "dropdownField": [
    #       ("timeline-day-filter-current-selection", "All"),
    #       ("timeline-view-selector-current-selection", "Sort by dates"),
    #   ],
    #   "assertData": (By.XPATH, "//h5[contains(.,\'Wednesday, 27 November 2024\')]")
    # },
    # {
    #   "id": "test_overdueSortByDate",
    #   "dropdownField": [
    #       ("timeline-day-filter-current-selection", "Overdue"),
    #       ("timeline-view-selector-current-selection", "Sort by dates"),
    #   ],
    #   "assertData": (By.XPATH, "//h5[contains(.,\'Wednesday, 27 November 2024\')]")
    # },
    # {
    #   "id": "test_dueNext7SortByDate",
    #   "dropdownField": [
    #       ("timeline-day-filter-current-selection", "Next 7 days"),
    #       ("timeline-view-selector-current-selection", "Sort by dates"),
    #   ],
    #   "assertData": (By.XPATH, "//h5[contains(.,\'Wednesday, 27 November 2024\')]")
    # },
    # {
    #   "id": "test_dueNext30SortByCourse",
    #   "dropdownField": [
    #       ("timeline-day-filter-current-selection", "Next 30 days"),
    #       ("timeline-view-selector-current-selection", "Sort by courses"),
    #   ],
    #   "assertData": (By.XPATH, "//h5[contains(.,\'Wednesday, 27 November 2024\')]")
    # },
    # {
    #   "id": "test_dueNext3MonthByCourse",
    #   "dropdownField": [
    #       ("timeline-day-filter-current-selection", "Next 3 months"),
    #       ("timeline-view-selector-current-selection", "Sort by courses"),
    #   ],
    #   "assertData": (By.XPATH, "//h5[contains(.,\'Wednesday, 27 November 2024\')]")
    # },
    # {
    #   "id": "test_dueNext6MonthByCourse",
    #   "dropdownField": [
    #       ("timeline-day-filter-current-selection", "Next 6 months"),
    #       ("timeline-view-selector-current-selection", "Sort by courses"),
    #   ],
    #   "assertData": (By.XPATH, "//h5[contains(.,\'Wednesday, 27 November 2024\')]")
    # },
]
