task_list=list(range(1,197244))

random.shuffle(task_list)

a=len(task_list)/2

task_l=task_list[:98621]

Task.objects.update(status='UNREAD')

len(task_l)
98621

len(task_list)
197243

Task.objects.filter(id__in=task_l).count()
97914

Task.objects.filter(id__in=task_l).update(status='READ')
97914

Task.objects.values('status').annotate(count=Count('status'))
[{'status': u'READ', 'count': 97914}, {'status': u'UNREAD', 'count': 97948}]