

# 🛍 Sparta Market DRF

DRF(Django Rest Framework)를 활용한 중고 거래 마켓 API 서버

## 📋 프로젝트 개요

- **프로젝트 이름**: sparta_market_DRF
- **개발 인원**: 1명
- **개발 환경**: Python 3.11, Django 4.2, DRF 3.14

## 🛠 기술 스택

### Backend
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
- ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white)
- ![DRF](https://img.shields.io/badge/Django_Rest_Framework-092E20?style=flat-square&logo=Django&logoColor=white)

### Database
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white)

### Tools
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white)
- ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white)

## 📌 주요 기능

### 1. 계정 관리
- 회원가입
- 로그인/로그아웃
- 프로필 조회
- 프로필 수정
- 비밀번호 변경
- 회원 탈퇴

### 2. 상품 관리
- 상품 등록
- 상품 목록 조회
- 상품 상세 조회
- 상품 수정
- 상품 삭제

### 3. 부가 기능
- 상품 검색 및 필터링
- 카테고리 관리
- 상품 좋아요
- 유저 팔로우
- 태그 시스템

## 📁 프로젝트 구조
```
sparta_market_DRF/
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── products/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
└── README.md
```

## 🔍 API 명세

### 계정 관련 API
| Method | Endpoint | 기능 | 인증 필요 |
|--------|----------|------|-----------|
| POST | /api/accounts/ | 회원가입 | X |
| POST | /api/accounts/login/ | 로그인 | X |
| POST | /api/accounts/logout/ | 로그아웃 | O |
| GET | /api/accounts/<username>/ | 프로필 조회 | O |
| PUT | /api/accounts/<username>/ | 프로필 수정 | O |
| PUT | /api/accounts/password/ | 비밀번호 변경 | O |
| DELETE | /api/accounts/ | 회원 탈퇴 | O |

### 상품 관련 API
| Method | Endpoint | 기능 | 인증 필요 |
|--------|----------|------|-----------|
| POST | /api/products/ | 상품 등록 | O |
| GET | /api/products/ | 상품 목록 조회 | X |
| GET | /api/products/<id>/ | 상품 상세 조회 | X |
| PUT | /api/products/<id>/ | 상품 수정 | O |
| DELETE | /api/products/<id>/ | 상품 삭제 | O |
| POST | /api/products/<id>/like/ | 상품 좋아요 | O |

## 📝 요구사항 체크리스트

### 필수 구현
- [x] 회원가입
- [x] 로그인
- [x] 프로필 조회
- [x] 상품 등록
- [x] 상품 목록 조회
- [x] 상품 수정
- [x] 상품 삭제

### 도전 구현
- [x] 로그아웃
- [x] 프로필 수정
- [x] 비밀번호 변경
- [x] 회원 탈퇴
- [x] 상품 검색 및 필터링
- [x] 카테고리 기능
- [x] 팔로잉 시스템
- [x] 좋아요 기능
- [x] 태그 기능
