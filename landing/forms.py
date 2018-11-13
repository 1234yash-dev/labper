import datetime
from collections import OrderedDict

from .models import Course, Lab, Profile, Teacher
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.forms.widgets import SelectDateWidget, TimeInput

from landing.models import Problem, Student, Submission


class DateInput(forms.DateInput):
    input_type = 'date'


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCourseForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['code', 'name', 'target_batch', 'session']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)
        self.fields['name'].label = 'Course Name'
        self.fields['code'].label = 'Course Code'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-input',
            'placeholder': 'Introduction to Example Technology'
        })
        self.fields['code'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'placeholder': 'CSX0X or ITX0X'
        })

        self.fields['target_batch'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

        self.fields['session'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
            'placeholder': '20XX-XY'
        })

    class Meta:
        model = Course
        fields = {'name', 'code', 'session', 'target_batch'}


class EditCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCourseForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['code', 'name', 'target_batch', 'session']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)
        self.fields['name'].label = 'Course Name'
        self.fields['code'].label = 'Course Code'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-input',
        })

        self.fields['code'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

        self.fields['target_batch'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

        self.fields['session'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
        })

    class Meta:
        model = Course
        fields = {'name', 'code', 'session', 'target_batch'}


class AddStudentForm(forms.Form):
    roll_no = forms.CharField(max_length=9)

    class Meta:
        fields = {'roll_no'}


class AddAssistantForm(forms.Form):
    roll_no = forms.CharField(max_length=9)

    class Meta:
        fields = {'roll_no'}


class AddLabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddLabForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['number', 'start_time', 'end_time', 'description']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)

        self.fields['number'].label = 'Lab Number'
        self.fields['start_time'].label = "Start Time"
        self.fields['end_time'].label = "End Time"
        self.fields['description'].label = "Description"

        self.fields['number'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'placeholder': 'Eg: 2',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'uk-textarea uk-input',
            'placeholder': 'Add description here',
        })
        self.fields['start_time'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })
        self.fields['end_time'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

    class Meta:
        model = Lab
        fields = {'number', 'start_time', 'end_time', 'description'}
        dateTimeOptions = {
            'autoclose': True,
            'startDate': str(datetime.datetime.today().date()),
            'endDate': str(datetime.datetime.today().date() + datetime.timedelta(7)),
            'format': 'mm/dd/yyyy hh:ii',
        }
        widgets = {
            'start_time': DateTimeWidget(options=dateTimeOptions),
            'end_time': DateTimeWidget(options=dateTimeOptions),
        }


class AddProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddProblemForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['title', 'content', 'similar', 'correctcode']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)
        self.fields['title'].label = 'Problem Title'
        self.fields['content'].label = 'Problem Content'
        self.fields['similar'].label = 'Similarity Percentage'
        self.fields['correctcode'].label = 'Correct Code'

        self.fields['title'].widget.attrs.update({
            'class': 'uk-input',
            'placeholder': 'Problem - 1: Fibbonaci'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'uk-input uk-textarea',
            'placeholder': 'You have ....'
        })

        self.fields['similar'].widget.attrs.update({
            'class': 'uk-input uk-textarea',
            'placeholder': 'Percentage Similarity Allowed'
        })

        self.fields['correctcode'].widget.attrs.update({
            'class': 'uk-input uk-textarea',
            'placeholder': 'Enter the correct code for the problem'
        })

    class Meta:
        model = Problem
        fields = {'title', 'content', 'similar', 'correctcode'}


class SubmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        self.fields['code_file'].label = 'Code File'

        self.fields['code_file'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'type': 'file'
        })

    class Meta:
        model = Submission
        fields = {'code_file', }


class ExtendDeadlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCourseForm, self).__init__(*args, **kwargs)
        self.fields['end_time'].label = 'Deadline'
        self.fields['end_time'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

    class Meta:
        model = Lab
        fields = {'end_time'}
        dateTimeOptions = {
            'autoclose': True,
            'startDate': str(datetime.datetime.today().date()),
            'endDate': str(datetime.datetime.today().date() + datetime.timedelta(7)),
            'format': 'mm/dd/yyyy hh:ii',
        }
        widgets = {
            'end_time': DateTimeWidget(options=dateTimeOptions),
        }