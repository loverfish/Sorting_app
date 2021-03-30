from django.db import models


class Post(models.Model):
    BUBBLE_SORT = 'BS'
    INSERTIONS_SORT = 'IS'
    MERGE_SORT = 'MS'
    SELECTION_SORT = 'SS'
    ALGORITHM_TYPE_SORT = [
        (BUBBLE_SORT, 'BUBBLE_SORT'),
        (INSERTIONS_SORT, 'INSERTIONS_SORT'),
        (MERGE_SORT, 'MERGE_SORT'),
        (SELECTION_SORT, 'SELECTION_SORT'),
    ]
    file = models.FileField(upload_to='files/')
    algorithm_type = models.CharField(
        max_length=2,
        choices=ALGORITHM_TYPE_SORT,
        default=BUBBLE_SORT,
    )
    start_list = models.TextField(blank=True)
    sorted_list = models.TextField(default=[])
    time_to_sort = models.FloatField()
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
