from rest_framework import serializers
from .models import Student, Teacher, Course


class CourseSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_duration(self, obj):
        return (obj.end_date - obj.start_date).days + 1

    def validate(self, data):
        """
        Check if the end date is after the start date
        """
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError(
                {"end_date": "End date must be later than start date"}
            )
        return data


class NestedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "id"


class StudentSerializer(serializers.ModelSerializer):
    courses = NestedCourseSerializer(many=True)

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        course_id_dicts = validated_data.pop("courses")
        print(course_id_dicts[0].keys())
        course_ids = [c["id"] for c in course_id_dicts]
        student = Student.objects.create(**validated_data)
        courses = []
        for c_id in course_ids:
            # UNSAFE
            course = Course.objects.get(id=c_id)
            courses.append(course)
        student.courses.add(*courses)
        return student


class TeacherSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Teacher
        fields = "__all__"
