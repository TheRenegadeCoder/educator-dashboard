from numpy import int64
import pandas as pd
from dash import dcc

from core.constants import *


def load_assignment_survey_data() -> dcc.Store:
    """
    Loads the assignment survey data from the remote CSV, cleans it, and computes
    some important metrics. The result is returned as a store object.

    :return: the assignment survey data as a store
    """
    # Load necessary data
    assignment_survey_data = pd.read_csv(URL_ASSESSMENT_REVIEWS)
    assignment_lookup = pd.read_csv(URL_ASSESSMENTS)
    assignment_group_lookup = pd.read_csv(URL_ASSESSMENT_GROUPS)
    survey_df = assignment_survey_data \
        .merge(assignment_lookup, on=COLUMN_ASSESSMENT_ID) \
        .merge(assignment_group_lookup, on=COLUMN_ASSESSMENT_GROUP_ID)
        
    # Sets types of columns
    survey_df["DateTime"] = pd.to_datetime(
        assignment_survey_data["DateTime"],
        format="%Y/%m/%d %I:%M:%S %p %z",
        utc=True
    )
        
    return dcc.Store(id=ID_ASSIGNMENT_SURVEY_DATA, data=survey_df.to_json())


def load_sei_data() -> dcc.Store:
    """
    Loads the SEI data from the remote CSV. The result is returned as a store 
    object.

    :return: the SEI data as a store
    """
    sei_data = pd.read_csv(URL_SEI_INSTRUCTOR_SCORES)
    teaching_history = pd.read_csv(URL_TEACHING_HISTORY)
    course_lookup = pd.read_csv(URL_COURSES)
    question_lookup = pd.read_csv(URL_SEI_QUESTIONS_LOOKUP)
    sei_ratings_history = sei_data \
        .merge(teaching_history, on=COLUMN_SECTION_ID) \
        .merge(course_lookup, on=COLUMN_COURSE_ID) \
        .merge(question_lookup, on=COLUMN_QUESTION_ID)

    return dcc.Store(id=ID_SEI_DATA, data=sei_ratings_history.to_json())


def load_sei_comments_data() -> dcc.Store:
    """
    Loads the SEI comment data from the remote CSV. The result is returned as a 
    store object.

    :return: the SEI comment data as a store 
    """
    sei_comment_data = pd.read_csv(URL_SEI_COMMENTS_HISTORY)
    return dcc.Store(id=ID_SEI_COMMENTS_DATA, data=sei_comment_data.to_json())


def load_course_eval_data() -> dcc.Store:
    """
    Loads the course evaluation data from the remote CSV. The result is returned 
    as a store object.

    :return: the SEI course evaluation data as a store
    """
    course_eval_data = pd.read_csv(URL_EVALUATION_SURVEY_HISTORY)

    # Sets types of columns
    course_eval_data["Timestamp"] = pd.to_datetime(
        course_eval_data["Timestamp"],
        format="%Y/%m/%d %I:%M:%S %p %Z"
    )

    return dcc.Store(id=ID_COURSE_EVAL_DATA, data=course_eval_data.to_json())


def load_education_data() -> dcc.Store:
    """
    Loads the grade data from the remote CSV. The result is returned as a store 
    object. 

    :return: the grade data as a store
    """
    grading_history = pd.read_csv(URL_ASSESSMENT_GRADES)
    teaching_history = pd.read_csv(URL_TEACHING_HISTORY)
    assignment_lookup = pd.read_csv(URL_ASSESSMENTS)
    assignment_group_lookup = pd.read_csv(URL_ASSESSMENT_GROUPS)
    course_lookup = pd.read_csv(URL_COURSES)
    education_data = grading_history \
        .merge(assignment_lookup, on=COLUMN_ASSESSMENT_ID) \
        .merge(assignment_group_lookup, on=COLUMN_ASSESSMENT_GROUP_ID) \
        .merge(teaching_history, on=COLUMN_SECTION_ID) \
        .merge(course_lookup, on=COLUMN_COURSE_ID)
    return dcc.Store(id=ID_EDUCATION_DATA, data=education_data.to_json())
