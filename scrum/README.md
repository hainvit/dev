## Scrum

### 1. Các khái niệm cơ bản trong Sprint
* Product Backlog: Là một file liệt kế tất cả các tính năng của Produc mà từ đó là cơ sở để xây dựng Sprint
* Story: Các feature của Product được đưa vào Product Backlog được gọi là story
* Sprint: Tập hợp các story cần hoàn thành trong một khung thời gian và sản phẩm sẽ release các tính năng đó (khung thời gian lý tưởng được chọn là 2 or 3 tuần)
* Các bên tham gia vào Scrum
  * Product Owner: Defined ra product backlog
  * Scrum Master: Là người có vai trò giúp development hiểu được product backlog và hiểu được các yêu cẩu của product owner
  * Development: Là người triển khai các yêu của cuả product backlog ( nhóm này thường có 3-8 người)
* Các sự kiện trong Scrum:
  * Sprint Planing Meeting: Họp kế hoạch sprint để thống nhất các feature có trong product backlog và tính toán xem những sotry nào sẽ được đưa vào các sprint nào
  * Daily Scrum: Hằng ngày sẽ có một cuộc họp không kéo dài quá 15 phút, mỗi người trong nhóm không được phép nói quá 5 phút và cần trả lời 3 cấu hỏi
    * Hôm qua làm gì ?
    * Hôm nay làm gì ?
    * Có issues gì không ?
  * Sprint Review: Đây được coi là một buổi tổng kết sprint và demo cho product owner những gì đã được thực thi trong sprint vừa rồi
  * Sprint Retrospective: Họp cải tiến sprint, buổi này sẽ đưa ra những thứ mà spint vừa rồi làm chưa được tốt và cần cải tiến ở sprint tiếp theo. Thông thường thì buổi họp này được tiến hành sau mỗi Sprint
* Trong suốt Sprint:
  * Không cho phép bất kì sự thay đổi nào ảnh hưởng đến mục tiêu của Sprint
  * Thành phần của nhóm phát triển phải được giữ nguyên
  * Mục tiêu chất lượng không được cắt giảm
  * Phạm của mỗi cá nhân cần được làm rõ và thương lượng giữa Product Owner với Development
* Sprint dài nhất là 1 tháng, nếu kèo dài quá thì sẽ gia tăng sự phức tạp
* Hủy Sprint
  * Chỉ có product Owner mới có đủ thẩm quyền để hủy một Sprint
  * Khi hủy một Sprint thì các phần hoàn chỉnh được xem xét lại. Các phần của Product backlog chưa hoàn thành sẽ được ước lượng lại
  * Việc hủy một Sprint sẽ gây lãng phí tài nguyên, do mọi người phải họp lại để lên kế hoạch cho một Sprint mới. Việc hủy Sprint thường gây tổn hại nhất định cho Nhóm phát triển, và rất ít khi xảy ra

### 2. Product Backlog
* Product Backlog là một danh sách các yêu cầu, các sotry, hoặc các tính năng của sản phẩm. Đó là các thứ mà khách hàng yêu cầu và được mô tả bằng thuật ngữ của khách hàng
* Những story đó bao gồm các trường sau:
  * ID
  * Name: Tên của story
  * Importance: Mực độ quan trọng của story (Mục này để product owner điển), nó là một với khoảng các giữa các đơn vị là lớn để thấy được sự quan trọng của các story
  * Initial estimate: Về thời gian hoàn thành story, mục này sẽ được development điền và đánh giá nó
  * How to demo: Hình thức demo với mỗi story sẽ được thực hiện như nào
  * Notes
* Có thể thêm một số fields
  * Bug tracking ID
  * Requestor

### 3. Kế hoạch Sprint
* Các nguyên tắc bắt buộc để có thể tiến hàng họp kế hoạch Sprint
```
* Product Backlog đã được định hình thì mới có thể tiến hành cuộc họp lên kế hoạch cho Sprint
* Phải có sự có mặt của Product Owner, nếu không có mặt thì họ phải ủy quyền cho một ai đó để có thể  approved các yêu cầu
```
* Nếu các thứ trong product backlog chưa được hoàn thành sẽ không có cuộc họp nào cả
* Product Owner phải là người hiểu rõ từng story một
* Những người không phải Product Owner có thể bôt sung story vào Product Backlog. Nhưng họ không được gá importance cho story đó, Product Owner sẽ là người làm việc đó và estimate sẽ được gán bỏi development
* Kết quả của buổi lập kế hoạch Sprint phải đạt được
  * Xác định mục tiêu của Sprint
  * Danh sách các thành viên của nhóm
  * Xác định ngày demo sprint

### 4. Sơ kêt sprint
* Trong buổi sơ kết Sprint nên tập trung vào việc đã làm được những gì hơn là việc trình bày đã làm như nào
* Đưa các cải tiến trong sprint tiếp theo

### 5. Lập kế hoạch release và estimate hợp đồng như nào
* Lập kế hoạch phát hành giúp chúng ta trả lời câu hỏi "khi nào, hoặc muộn nhất, chúng ta sẽ có thể chuyển giao được phiên bản 1.0 của hệ thống mới này"
* Các cuộc họp phải tuân thủ khung thời gian
* Khi bắt đầu sprint mới thì sẽ dùng một khoảng thời gian để có thể vừa fix bug của Sprint trước mà vừa có thể làm Sprint mới
* Tập trung hoàn thành các tính năng của một Sprint, sau đó mới chuyển sang một Sprint mới


## Refs
* https://drive.google.com/file/d/1j4X1ORFev9e23e45w49J8B5Vz1T7V-AO/view?usp=sharing
* https://drive.google.com/file/d/1xmfPaNae1_w-CLxRtbseaigYFBmyi4Ve/view?usp=sharing