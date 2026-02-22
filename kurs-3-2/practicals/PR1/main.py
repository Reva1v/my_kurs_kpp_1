import cv2
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, 'test_image.png')

image = cv2.imread(IMAGE_PATH, cv2.IMREAD_UNCHANGED)

print('=' * 55)
print('1. Масив зображення (перші 2 рядки пікселів):')
print(image[:2])
print(f'\n   img.shape = {image.shape}')


print('\n' + '=' * 55)
print('2. Розміри зображення:')
height, width, channels = image.shape
print(f'   Висота  : {height} пікселів')
print(f'   Ширина  : {width} пікселів')
print(f'   Канали  : {channels}')


print('\n' + '=' * 55)
print('3. Об\'єм зображення в байтах:')


size1 = height * width * channels * image.itemsize
print(f'   Спосіб 1 (height × width × channels × itemsize): {size1} байт')


size2 = image.size * image.itemsize
print(f'   Спосіб 2 (img.size × img.itemsize)             : {size2} байт')
print(f'   (img.size = {image.size}, img.itemsize = {image.itemsize})')


img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 5))
plt.imshow(img_rgb)
plt.title('Оригінальне зображення')
plt.axis('off')
plt.tight_layout()
plt.show()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title('Звичайне сіре зображення')
axes[0].axis('off')

axes[1].imshow(gray_image, cmap='gray', vmin=80, vmax=180)
axes[1].set_title('Зображення з ручним масштабуванням діапазону значень')
axes[1].axis('off')

plt.tight_layout()
plt.show()


print('\n' + '=' * 55)
print('6. Збереження зображень у форматі JPEG:')

for q in [75, 30, 0]:
    out_path = os.path.join(BASE_DIR, f'image_quality_{q}.jpg')
    cv2.imwrite(out_path, image, [cv2.IMWRITE_JPEG_QUALITY, q])
    size_kb = os.path.getsize(out_path) / 1024
    print(f'   Якість {q:3d}% -> {os.path.basename(out_path)}  ({size_kb:.1f} KB)')


print('\n' + '=' * 55)
print('7. Відкриття збережених зображень стандартними засобами ОС...')

for q in [75, 30, 0]:
    filepath = os.path.join(BASE_DIR, f'image_quality_{q}.jpg')
    os.startfile(filepath)

print('\nГотово!')
