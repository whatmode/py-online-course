from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        days_in_weeks = days / 7
        return ceil(days_in_weeks)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        days = course_dict.get("days")
        if days is not None:
            weeks = cls.days_to_weeks(days)
            return cls(course_dict["name"], course_dict["description"], weeks)
