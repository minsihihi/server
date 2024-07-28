# Generated by Django 5.0.3 on 2024-07-28 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MediCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_distance', models.CharField(default='', max_length=20)),
                ('hospital_name', models.CharField(max_length=20)),
                ('hospital_category', models.CharField(max_length=20)),
                ('hospital_tel', models.CharField(max_length=15)),
                ('hospital_ratings', models.CharField(max_length=20)),
                ('hospital_open', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('medicard', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='medicarrier.medicard')),
                ('name', models.CharField(default='이름', max_length=20)),
                ('sex', models.CharField(choices=[('남', '남'), ('여', '여')], max_length=20)),
                ('nationality', models.CharField(default='국적', max_length=20)),
                ('name_eng', models.CharField(default='영문 이름', max_length=20)),
                ('birthdate', models.DateField()),
                ('height', models.CharField(default='키', max_length=20)),
                ('weight', models.CharField(default='몸무게', max_length=20)),
                ('bloodtype', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=20)),
                ('pregnant', models.CharField(choices=[('임신중', '임신중'), ('임신 중 아님', '임신 중 아님'), ('가능성 있음', '가능성 있음')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MediInfo',
            fields=[
                ('medicard', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='medicarrier.medicard')),
                ('condition', models.CharField(default='현재 증상 없음', max_length=20)),
                ('illness', models.CharField(default='없음', max_length=20)),
                ('medicine', models.CharField(default='복용하는 약 없음', max_length=20)),
                ('allergy', models.CharField(default='알레르기 없음', max_length=20)),
                ('diagnosis', models.CharField(default='근 n개월 이내 없음', max_length=20)),
                ('surgery', models.CharField(default='근 n개월 이내 없음', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Assist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(choices=[('약국', '약국'), ('병원', '병원')], default='', max_length=20)),
                ('hospital_type', models.CharField(choices=[('내과', '내과'), ('외과', '외과'), ('정형외과', '정형외과'), ('이비인후과', '이비인후과'), ('응급실', '응급실'), ('산부인과', '산부인과'), ('피부과', '피부과'), ('치과', '치과'), ('안과', '안과'), ('비뇨기과', '비뇨기과'), ('신경외과', '신경외과'), ('항문외과', '항문외과'), ('성형외과', '성형외과'), ('정신건강의학과', '정신건강의학과')], default='', max_length=20)),
                ('symptom_type', models.CharField(choices=[('콧물이 나요', '콧물이 나요'), ('열이 나요', '열이 나요'), ('인후통이 있어요', '인후통이 있어요'), ('귀가 아파요', '귀가 아파요'), ('기침을 해요', '기침을 해요')], default='', max_length=20)),
                ('symptom_etc', models.CharField(blank=True, max_length=20, null=True)),
                ('symptom_start', models.CharField(choices=[('오늘', '오늘'), ('1일 전', '1일 전'), ('2-3일 전', '2-3일 전'), ('일주일 전', '일주일 전'), ('일주일 이상', '일주일 이상')], default='', max_length=20)),
                ('symptom_freq', models.CharField(choices=[('지속적', '지속적'), ('간헐적', '간헐적'), ('특정 시간에만', '특정 시간에만')], default='', max_length=20)),
                ('illness_etc', models.CharField(default='없', max_length=20)),
                ('medicine_etc', models.CharField(default='없습', max_length=20)),
                ('etc', models.CharField(blank=True, max_length=20, null=True)),
                ('ins_req1', models.CharField(choices=[('질병', '질병'), ('상해', '상해')], default='', max_length=20)),
                ('ins_req2', models.CharField(choices=[('입원', '입원'), ('통원', '통원'), ('후유장해', '후유장해'), ('수술', '수술'), ('진단', '진단')], default='', max_length=20)),
                ('hospital_fee', models.CharField(choices=[('3만원 미만', '3만원 미만'), ('3만원 이상 ~ 10만원 미만', '3만원 이상 ~ 10만원 미만'), ('10만원 이상', '10만원 이상')], default='', max_length=20)),
                ('disease_detail', models.CharField(choices=[('암', '암'), ('뇌질환', '뇌질환'), ('심질환', '심질환'), ('기타', '기타')], default='', max_length=20)),
                ('document', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recommended_hospitals', models.ManyToManyField(blank=True, related_name='recommended_by_assists', to='medicarrier.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_type', models.CharField(max_length=20)),
                ('insturance_name', models.CharField(max_length=20)),
                ('insurance_call', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
