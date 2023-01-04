def facial_keypoints_all(img):
    keypoints_list = []
    img_itr = image_copy(img)  
    face_count = 0
    flag_check_face = True    
    while flag_check_face:
        try: 
            keypoints_curr = facial_keypoints(img_itr)
            keypoints_list.append(keypoints_curr)
            face_count += 1
            start_i = (keypoints_curr[20-1])[1]
            start_j = (keypoints_curr[1-1])[0]
            end_i = (keypoints_curr[9-1])[1]
            end_j = (keypoints_curr[17-1])[0]    
            img_itr[start_i:end_i, start_j:end_j ] = 255
        except: 
            flag_check_face = False
    return keypoints_list

def draw_keypoints_all(img, keypoints_list, pointsize):
    img_itr = image_copy(img)
    for keypoints in keypoints_list:
        img_itr = draw_keypoints(img_itr, keypoints, size = pointsize)
        
    return img_itr
def compare(kp1, kp2):
    for i in range(len(kp1)):
        flag = True
        cont = True
        a = int(str(kp1[i][0][0]))-int(str(kp2[0][0]))
        b = int(str(kp1[i][0][1]))-int(str(kp2[0][1]))
        for j in range(68):
            if not a-10 <= int(str(kp1[i][j][0])) - int(str(kp2[j][0])) <= a+10 and not b-10 <= int(str(kp1[i][j][1])) - int(str(kp2[j][1])) <= b+10 and cont:
                flag = False
                cont = False
        if flag:
            return i

url = "http://senses‹tudy-server/api/resource/public/accountstorage-objs/2227a6fe-85c3-4b3a-ac8f-8f84a4210ba9/find6.jpg"
img1 = image_read(url)
figure() + image(img1)
kp1 = facial_keypoints_all(img1)
#all = draw_keypoints_all(img1, kp1, 4)
#figure() + image(all)

person = "http://sensestudy-server/api/resource/public/accountstorage-objs/2227a6fe-85c3-4b3a-ac8f-8f84a4210ba9/person.jpg"
img2 = image_read(person)
figure() + image(img2)
kp2 = facial_keypoints(img2)
#print(kp2)
#person_img = draw_keypoints(img2, kp2)
#figure() + image(person_img)

index = compare(kp1, kp2)
final = draw_keypoints(img1, kp1[index], size=5)
figure() + image(final)
