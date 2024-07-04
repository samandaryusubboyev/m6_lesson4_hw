import uuid

class SaveMedia(object):
    def save_book_image_path(instance, filename):
        image_path = filename.split('.')[-1]
        return f"book/{uuid.uuid4()}.{image_path}"

#
# if __name__ == '__main__':
#     filename = "download.png"
#     image_path = filename.split('.')[-1]
#     return f"book/{uuid.uuid4()}.{image_path}"