from django.db import models


class Post(models.Model):
    BUBBLE_SORT = 'BS'
    INSERTIONS_SORT = 'IS'
    MERGE_SORT = 'MS'
    ALGORITHM_TYPE_SORT = [
        (BUBBLE_SORT, 'BUBBLE_SORT'),
        (INSERTIONS_SORT, 'INSERTIONS_SORT'),
        (MERGE_SORT, 'MERGE_SORT'),
    ]
    file = models.FileField(upload_to='files/')
    algorithm_type = models.CharField(
        max_length=2,
        choices=ALGORITHM_TYPE_SORT,
        default=BUBBLE_SORT,
    )
    sorted_list = models.TextField(default=[1])
    time_to_sort = models.FloatField()

    def __str__(self):
        return self.file.name
