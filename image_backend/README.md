# Backend
## Get Started

1. Please input available AWS Credential to test. You can test with local storage if `USE_S3` is `False`
2. `cd image_backend/`
3. Start a virtual environment (if desired)
4. Install requirements `pip install -r requirements.txt`
5. `python manage.py runserver`


## Model

### Images
- option
- original_image
- square_image
- small_image

## API
[POST] `http://localhost:8000/api/upload`

### Body
```
{
  'option':'OG' ('SQ', 'SM', 'AL'),
  'origin_image': base64 string
}
```

### Response
```
{
  "message": "Save image successfully",
  "code": 200
}
```
```
{
  "message": "Please select image file",
  "code": 400
}
```
```
{
  "message": "Can not save image: {trackback}",
  "code": 400
}
```