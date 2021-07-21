from rest_framework import serializers
from .models import Student, Teacher, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_duration(self, obj):
        return (obj.end_date - obj.start_date).days
    
    def validate(self, data):
        """
            Check if the end date is after the start date
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"end_date": "End date must be later than start date"})
