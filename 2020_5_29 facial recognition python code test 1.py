import cv2 as cv
import dlib

detector = dlib.get_frontal_face_detector()

color = ('b', 'g', 'r')
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 650)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 500)

near_threshold = 0.01

while(cap.isOpened()):
    ret, frame = cap.read()
    face_rects, scores, idx = detector.run(frame, 0)

    for i, d in enumerate(face_rects):
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()

        faceLong = y2-y1
        upface = frame[y1:y1+int(1/3*faceLong), x1:x2]
        downface = frame[y1+int(1/3*faceLong):y2, x1:x2]

        hist1 = cv.calcHist([upface], [0, 1, 2], None, [
                            256, 256, 256], [0, 256, 0, 256, 0, 256])
        hist2 = cv.calcHist([downface], [0, 1, 2], None, [
                            256, 256, 256], [0, 256, 0, 256, 0, 256])

        # 平移縮放
        cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
        cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)

        near = cv.compareHist(hist1, hist2, 0)
        if(near < near_threshold):
            # 畫框框與寫字
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv.LINE_AA)
            cv.putText(frame, "Wear Mask", (x1, y1),
                       cv.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 1, cv.LINE_AA)
        else:
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 4, cv.LINE_AA)
            cv.putText(frame, "No Mask", (x1, y1),
                       cv.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 1, cv.LINE_AA)

    cv.imshow("Face Detection", frame)

    if(cv.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv.destroyAllWindows()
