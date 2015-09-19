from django.db import models

# Create your models here.
class masterClass(models.Model) :
    classID = models.CharField(max_length = 100)  #班级ID
    className = models.CharField(max_length = 50, blank = True)  #班级名称
    classStudentID = models.ForeignKey(masterStudent)  #学生ID
    createTime = models.DateTimeField(auto_now_add = True)  #创建日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

class masterLesson(models.Model) :
    lessonID = models.CharField(max_length = 100)  #课程ID
    lessonName = models.CharField(max_length = 50, blank = True)  #课程名称
    createTime = models.DateTimeField(auto_now_add = True)  #创建日期

class masterStudent(models.Model) :
    studentID = models.CharField(max_length = 100)  #学生ID
    studentName = models.CharField(max_length = 50, blank = True)  #学生姓名
    createTime = models.DateTimeField(auto_now_add = True)  #创建日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

class masterTeacher(models.Model) :
    teacherID = models.CharField(max_length = 100)  #教师ID
    teacherName = models.CharField(max_length = 50, blank = True)  #教师姓名
    createTime = models.DateTimeField(auto_now_add = True)  #创建日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

class transSchedule(models.Model) :
    scheduleTimeStart = models.ForeignKey(Question)
    scheduleTimeEnd = models.ForeignKey(Question)
    scheduleTeacherID = models.CharField(max_length = 100)  #教师ID
    scheduleStudentID = models.CharField(max_length = 100)  #学生ID
    scheduleLessonID = models.CharField(max_length = 100)  #课程ID
    scheduleClassID = models.CharField(max_length = 100)  #班级ID
