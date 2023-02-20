from dataclasses import fields
from rest_framework import serializers
from lmsmainapp.models import *

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields='__all__'

class examSerializer(serializers.ModelSerializer):
    class Meta:
        model=exam
        fields='__all__'

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=course
        fields='__all__'

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields='__all__'

class topicSerializer(serializers.ModelSerializer):
    class Meta:
        model=topic
        fields='__all__'

class subtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subtopics
        fields='__all__'

class exam_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model=exam_master
        fields='__all__'

class examQuestionallocationSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=exam_question_allocation
        fields='__all__'

class question_bankSerializer(serializers.ModelSerializer):
    class Meta:
        model=question_bank
        fields = '__all__'


class question_bank_optionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=question_bank_options
        fields='__all__'

#mcq+++++++++++++++++++++++++++++++++++++++

class optSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_bank_options
        fields = ['identifier','choice']

class qustnSerializer(serializers.ModelSerializer):
    options = optSerializer(many=True, read_only=True)
    class Meta:
        model = question_bank
        fields = ['id','question', 'correct_answer','options']

class examQuestionallocationSerializer1(serializers.ModelSerializer):
     class Meta:
         model=exam_question_allocation
         fields=['question']
##############################################

class questionOptionsSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = question_bank_options
        fields = ['id','choice','identifier']
        depth  = 1

class questionSerializer(serializers.ModelSerializer):
    options = optSerializer(many=True, read_only=True)
    #options = questionOptionsSerializer(many=True,read_only=True)
    class Meta: 
        model = question_bank
        fields = ['id','question','no_of_options','options']
        depth  = 1
        
               
class examdetailsSerializer(serializers.ModelSerializer):
    options = optSerializer(many=True, read_only=True)
    question1 = questionSerializer(many=True,read_only=True)
    class Meta: 
        model = exam_question_allocation
        fields = ['id','question','question1','options']
        depth  = 1




class VideoclassSerializer(serializers.ModelSerializer):
    class Meta:
        model=video_class
        fields='__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=videocomment
        fields='__all__'



class courseSubjectallocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=course_subject_allocation
        fields='__all__'

class topicCourseAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=topic
        fields='__all__'



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=banner
        fields='__all__'


class DetailsresultSerializer(serializers.ModelSerializer):
    class Meta:
        model=result_details
        fields = ['id','question','attempted_time','is_flagged','user_answer','correct_answer','options_switched','switched_wrong_correct','switched_correct_wrong']

class ExamrstSerializer(serializers.ModelSerializer):
    attent = DetailsresultSerializer(many=True)
    class Meta:
        model=examresult
        fields = ['id','user','exam','datetime','total_correct','total_wrong','total_skipped','flagged_correct','flagged_attempt','final_score','attent']
    def create(self, validated_data):
        exam_data = validated_data.pop('attent')
        results = examresult.objects.create(**validated_data)
        for exam_data in exam_data:
            result_details.objects.create(examresult=results, **exam_data)
        return results




class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model=syllabus
        fields='__all__'



class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=notes
        fields='__all__'