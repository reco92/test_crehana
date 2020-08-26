from django.db import connection
from django.core.management.base import BaseCommand

from core.models import ProgressVideo, Registration, Course, Category

class Command(BaseCommand):
    help = 'Migration'


    def mysql_migration():
        """
        This should work on mysql scenario
        """

        with connection.cursor() as cursor:
            print("Connected. Starting command")
            query1 = """
                UPDATE 
                    core_progressvideo AS cp
                INNER JOIN
                    core_registration cr ON (cp.course_id = cr.course_id AND cp.user_id = cp.user_id)
                SET 
                    cp.registration_id = cr.id
                """
            cursor.execute(query1)
            query2 = """
                UPDATE 
                    core_progressvideo AS cp
                INNER JOIN core_course cc ON cp.course_id = cc.id
                INNER JOIN core_category cca ON cc.category_id = cca.id
                SET 
                    cp.category_id = cca.id
                """
            cursor.execute(query2)
            print('Query executed')


    def handle(self, *args, **options):

        # self.mysql_migration()

        map_registration = dict()
        map_categories = dict()

        categories = Category.objects.all()
        for item in categories:
            map_categories[item.id] = item

        all_regs = Registration.objects.all().select_related('course', 'user')
        all_courses = Course.objects.all()

        for item in all_courses:
            map_registration[item.id] = dict()

        for item in all_regs:
            map_registration[item.course.id][item.user.id] = item 

        all_progress = ProgressVideo.objects.all().select_related('course', 'user')
        for item in all_progress:
            item.category = map_categories[item.course.id]
            item.registration = map_registration[item.course.id][item.user.id]

        ProgressVideo.objects.bulk_update(all_progress, ['category', 'registration'])



        






        