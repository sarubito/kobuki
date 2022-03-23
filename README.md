# For kobuki　sample program

## What's kobuki?
![image](https://user-images.githubusercontent.com/61666505/159632989-1f8e4d19-d8c8-49c4-9b3e-2b9a8e5ba435.png) <br>
kobukiは研究開発用途を目的とした、オープンソースモバイルロボットです。<br>

kobukiに搭載されているセンサ一覧
- ジャイロセンサ
- エンコーダ
- バンパ
- 赤外線測距センサ

## kobukiの動かし方(キーボード操作編)<br>
1. ``` roslaunch kobuki_node minimal.launch ```
2. ``` roslaunch kobuki_keyop keyop.launch ``` <br>
w, a, s, d で前、左、後、右に移動する。 <br>
