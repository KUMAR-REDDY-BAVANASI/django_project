from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError("The maximum file size can be uploaded is 10mb")
    else:
        return value