import pandas as pd

df = pd.DataFrame(
    [
        {
            "reference": "Mã môn học của môn Toán cho Khoa học máy tính là CS115. Tóm tắt nội dung môn học như sau: Môn này cung cấp kiến thức về Toán ứng dụng trong các lĩnh vực như máy học, trí tuệ nhân tạo, khai phá dữ liệu và xử lý tín hiệu số.",
            "query": "Môn CS115 học cái gì?",
            "response":"",
        },
        {
            "reference": "Cử nhân ngành Công nghệ Thông tin (Áp dụng từ Khoá 18 - 2023) ngành công nghệ thông tin việt nhật. Hình thức đào tạo: Chính quy tập trung. Số tín chỉ đào tạo: Tối thiểu 132 tín chỉ (bao gồm cả ngoại ngữ). Thời gian đào tạo: 04 năm (8 học kỳ chính).",
            "query": "Cử nhân ngành Công nghệ thông tin cần học mấy năm?",
            "response":"",
        },
        {
            "reference": "Môn Nhập môn mạng máy tính với mã IT005 cung cấp kiến thức cơ bản về các khái niệm như mạng máy tính, truyền dữ liệu, dịch vụ mạng và kỹ thuật mạng không dây.",
            "query": "Môn Nhập môn mạng máy tính học những gì?",
            "response":"",
        },
        {
            "reference": "Môn học CS221 về Xử lý ngôn ngữ tự nhiên nhằm cung cấp cho sinh viên những kiến thức cơ bản về chuyên ngành này, bao gồm văn phạm phi ngữ cảnh CFG, văn phạm DCG, cách cài đặt và giải thích cơ chế xử lý văn phạm DCG trên Prolog, và FSA.",
            "query": "CS221 là môn gì?",
            "response":"",
        },
        {
            "reference": "Môn học mang tên Lý Luận Kinh Tế Chính Trị Má́c - Lênin, với mã là SS008. Tổng quan chung về nội dung môn học, sinh viên sẽ được làm quen và nắm vững những nguyên lý cơ bản của Lý Luận Kinh Tế Chính Trị Má́c - Lênin.",
            "query": "Môn kinh tế chính trị Mác-Leenin là môn gì?",
            "response":"",
        },
        {
            "reference": "**Chú trọng vào những chủ đề then chốt, Môn Công nghệ Tường lửa và Bảo vệ Mạng Ngoài vi (NT311) chuyên sâu về:** Khái quát về Kiến trúc mạng an toàn, Nhu cầu cấp thiết của doanh nghiệp về bảo mật thông tin, Công nghệ Tường lửa và Mạng ngoài vi, Hệ thống lọc gói tin và Máy chủ Proxy, Mô hình hệ thống thực tế và giả định trong bảo mật mạng",
            "query": "Mã môn NT311 là của môn học nào?",
            "response":"",
        },
        {
            "reference": "Thông qua môn Chuyên đề M-commerce được mã hóa SE348, sinh viên sẽ được tiếp cận với những hoạt động sơ khai của thương mại di động (M-commerce). Nội dung môn học giúp sinh viên trang bị các kỹ năng thiết thực với kinh nghiệm thực hành ứng dụng trên các thiết bị di động không dây. Ngoài ra, môn học đào sâu nghiên cứu về công nghệ di động và ứng dụng vào lĩnh vực M-commerce, phân tích các lợi ích, ưu điểm, nhược điểm và cách thức áp dụng của thương mại di động. Bên cạnh đó, sinh viên cũng được hướng dẫn tìm hiểu sự khác biệt giữa thương mại di động và thương mại điện tử (E-commerce).",
            "query": "Chuyên đề M-commerce là chuyên đề gì vậy?",
            "response":"",
        },
        {
            "reference": "Môn học có tên gọi là CS338 và nó thuộc lĩnh vực Nhận dạng. Nội dung của môn học này bao gồm kiến thức cơ bản về các thuật toán nhận dạng có tham số và phi tham số như SVM, Mạng Neural Network, Mô Hình Markov Ẩn, Maximum Likelihood, K-Nearest Neighbor, K-Mean. Sinh viên có thể áp dụng các thuật toán này vào bài toán nhận dạng với dữ liệu đặc trưng được rút trích từ các dữ liệu thực tế.",
            "query": "môn học về các thuật toán nhận dạng như SVM, Maximum likelihood là môn gì nhỉ?",
            "response":"",
        },
        {
            "reference": "Môn học Xử lý song song được mã hóa là SE351. Tóm tắt nội dung như sau: Khóa học cung cấp cho sinh viên kiến thức cơ bản về thiết kế thuật toán song song hiệu quả như thiết kế thuật toán song song, phân tích hiệu suất của chương trình song song, lập trình đa luồng bằng POSIX, lập trình bằng OpenMP và ứng dụng các kỹ thuật lập trình song song để giải quyết bài toán khoa học.",
            "query":"Môn SE351 là môn gì? môn này học những kiến thức gì?",
            "response":"",  
        },
        {
            "reference": "Môn Công nghệ phần mềm chuyên sâu được mã hóa là SE214, tập trung truyền đạt kiến thức chuyên sâu về các phương pháp, quy trình phát triển phần mềm mới và tân tiến như RUP, Agile, XP, Scrum. Sinh viên sẽ được trang bị nền tảng vững chắc về đặc tả và công nghệ yêu cầu, cũng như làm quen với các kiến thức về quản lý và triển khai dự án phần mềm. Thông qua môn học này, sinh viên có thể nắm vững và vận dụng thành thạo các quy trình tiên tiến trong lĩnh vực công nghệ phần mềm, đồng thời có đủ năng lực thiết lập, quản lý và triển khai một dự án phần mềm một cách chuyên nghiệp.",
            "query": "Tôi muốn học Scrum, Agile,.. các cách quản lý dự án phần mềm thì nên học môn gì",
            "response":"",
        },
        {
            "reference": "Môn học CE409 là môn Kỹ thuật thiết kế kiểm tra. Nội dung môn học tóm tắt như sau: Môn học này giúp sinh viên hiểu về quy trình thiết kế và phát triển vi mạch số từ ý tưởng đến thiết kế, hiện thực và kiểm thử trên FPGA, trên SoC theo hướng ASIC. Sinh viên sẽ nắm được kiến thức và kỹ năng về các module ngoại vi, bộ xử lý, thiết kế mạch kiểm tra tích hợp bằng ngôn ngữ phần cứng hoặc ngôn ngữ cấp cao (C/C++) để kiểm tra hoạt động của vi mạch ngoại vi, vi mạch xử lý. Họ cũng sẽ có kỹ năng phân tích, đánh giá và kiểm tra mẫu thiết kế trên chip FPGA, cũng như phân tích và đánh giá các chức năng của các vi mạch thiết kế dựa trên kết quả mô phỏng.",
            "query": "Môn CE409 là môn gì? nội dung môn học này học những điều gì?",
            "response":"",
        },
        {
            "reference": "Môn học CS332 trong lĩnh vực Thị giác Máy tính tập trung vào việc giới thiệu các giải pháp kỹ thuật để áp dụng phương pháp máy học vào các bài toán quan trọng trong ngành Thị giác máy tính, bao gồm: phát hiện đối tượng (phát hiện khuôn mặt, phát hiện người đi bộ), nhận dạng (phân loại đối tượng, nhận dạng chi tiết), phân tích ngữ nghĩa và chỉ mục hóa.",
            "query":"Môn thị giác máy tính gồm những nội dung gì?",
            "response":"",
        },
        {
            "reference": "Môn học CS231 về Thị giác máy tính giới thiệu các kiến thức căn bản trong lĩnh vực này, bao gồm low-level computer vision và mid-level computer vision. Các chủ đề cụ thể bao gồm rút trích và khai thác thông tin trên ảnh, các loại đặc trưng thị giác cấp thấp và phương pháp biểu diễn đặc trưng thị giác cấp thấp, kĩ thuật so khớp ảnh, kĩ thuật phân đoạn ảnh và phương pháp theo vết (tracking).",
            "query":"Môn thị giác máy tính học những gì? mã môn này là môn gì?",
            "response":"",
        },
        {
            "reference": "Môn NT213 với tên gọi Bảo mật web và ứng dụng là một môn học cung cấp cái nhìn tổng quát về các kỹ thuật hack ứng dụng web. Sinh viên theo học sẽ được tiếp cận với các phương pháp bảo mật như thu thập thông tin, xác thực đầu vào từ phía máy chủ và bảo vệ các nền tảng phía máy khách. Ngoài ra, môn học còn trang bị kiến thức về phần mềm độc hại dành cho nền tảng web.",
            "query": "Môn bảo mật web và ứng dụng có nội dung môn học là gì?",
            "response":"",
        },
        {
            "reference": "Cử nhân ngành Khoa học Máy tính (Áp dụng từ khóa 18 - 2023) Hình thức đào tạo: Chính quy tập trung. Số tín chỉ đào tạo: 126 tín chỉ Cấp bằng: Cử nhân ngành Khoa học Máy tính. Thời gian đào tạo: 3.5 năm (gồm 7 học kỳ chính thức).",
            "query":"Cử nhân ngành khoa học máy tính khóa 18 cần học bao nhiêu tín chỉ?",
            "response":"",
        },
        {
            "reference": "Môn học ""Mẫu Thiết kế"" với mã khóa là SE401 cung cấp một cái nhìn sâu sắc về những mẫu thiết kế phổ biến trong phát triển phần mềm. Nội dung môn học tập trung vào việc khám phá các kiến trúc thiết kế linh hoạt, cho phép áp dụng các mẫu thiết kế hiệu quả trong nhiều tình huống khác nhau. Từ đó, sinh viên sẽ nắm vững các giải pháp thiết kế đa dạng, hỗ trợ đắc lực cho quá trình phát triển phần mềm thành công.",
            "query":"Môn SE401 là môn gì?",
            "response":"",
        },
        {
            "reference": "Môn Các vấn đề chọn lọc trong Thị giác máy tính (CS420) là một môn học có nội dung linh hoạt, tập trung chủ yếu vào các chủ đề và vấn đề mới nhất trong lĩnh vực này.",
            "query":"Môn CS420 có tên là gì?",
            "response":"",
        },
        {
            "reference": "Môn Thiết kế giao diện người dùng (IE106) trang bị kiến thức nền tảng về các vấn đề sử dụng hệ thống tương tác, nguyên tắc thiết yếu của thiết kế giao diện người dùng, quy trình thiết kế giao diện, đánh giá thiết kế giao diện; đồng thời giới thiệu các kỹ thuật liên quan đến thực đơn, nhập liệu, hộp thoại, tài liệu người dùng, giao diện tìm kiếm, mối liên kết giữa giao diện người dùng và trực quan hóa dữ liệu. Môn học cũng cung cấp cái nhìn tổng quan về những công nghệ mới trong lĩnh vực thiết kế giao diện người dùng.",
            "query": "IE106 học những gì?",
            "response":"",
        },
        {
            "reference": "Môn Anh văn 1 được định danh với mã môn học ENG01. Về nội dung, đây là môn học mở đầu trong chuỗi các học phần Anh văn bắt buộc trong chương trình đào tạo chính quy ở bậc đại học. Môn học cung cấp nền tảng kiến thức và kỹ năng dùng Anh ngữ trong môi trường công việc. Qua đó, sinh viên được kỳ vọng đạt trình độ Anh ngữ từ 30 đến dưới 42 điểm theo thang đánh giá toàn cầu GSE (The Global Scale of English), tương đương cấp độ tiền trung cấp (pre-intermediate A2-B1).",
            "query":"Học môn Anh văn 1 thì sẽ đạt được trình độ ngoại ngữ nào",
            "response":"",
        },
        {
            "reference": "Môn Control and Audit of Information Systems, hay còn được gọi là MSIS4243, là một khóa học cung cấp những quy trình xác thực, bảo quản và trích xuất các chứng cứ điện tử, bên cạnh đó còn hướng dẫn sinh viên giám sát và điều tra về những vụ xâm nhập vào hệ thống máy chủ và mạng, phân tích thông tin thu thập được, và chuẩn bị các bằng chứng xác thực đáp ứng được các yêu cầu. Khóa học cũng cung cấp các công cụ pháp lý và nguồn tài nguyên cần thiết cho các quản trị viên hệ thống, cũng như kiến thức về đạo đức, luật pháp, chính sách và các tiêu chuẩn liên quan đến bằng chứng số.",
            "query":"Môn MSIS4243 học những gì?",
            "response":"",
        },
        {
            "reference": "Môn học có tên là Tương tác người - Máy và mã môn học là CE406. Tóm tắt nội dung môn học như sau: ▪ Cung cấp định nghĩa về HCI, các đối tượng tham gia giao tiếp và các vấn đề liên quan. ▪ Giới thiệu các kỹ thuật giao tiếp truyền thống như giao tiếp dòng lệnh, menu, văn bản, các kỹ thuật hiện đại, giao tiếp đồ họa GUI, giao tiếp trực tiếp WIMP. ▪ Trình bày chuẩn và mô hình được sử dụng trong thiết kế và các phương pháp thiết kế. ▪ Giới thiệu các kỹ thuật đánh giá giao tiếp người dùng được sử dụng trong quá trình thiết kế và đánh giá sản phẩm.",
            "query": "Môn tương tác người - máy là môn gì nhỉ? mã môn này là gì",
            "response":"",
        },
        {
            "reference": "Môn Hệ điều hành có mã môn IT007, bao gồm 8 chương với nội dung về các khái niệm, nguyên tắc hoạt động cơ bản của hệ điều hành, trình bày từ cơ bản đến nâng cao. Nội dung cụ thể bao gồm: tổng quan về hệ điều hành, cấu trúc hệ điều hành, quản lý tiến trình, định thời CPU, đồng bộ hóa tiến trình, bế tắc, quản lý bộ nhớ và bộ nhớ ảo. Sau mỗi phần lý thuyết, sinh viên sẽ được thực hành trong phòng thí nghiệm để củng cố kiến thức và hiểu rõ hơn về các khái niệm, giải thuật đã học.",
            "query": "Môn IT007 có bao nhiêu chương?",
            "response": "",   
        },
        {
            "reference": "Môn IE105, còn được gọi là Nhập môn bảo đảm và an ninh thông tin, cung cấp các kiến thức cơ bản toàn diện về bảo đảm và an ninh thông tin. Nội dung của môn học bao gồm các nguyên tắc an ninh mạng nền tảng, phương pháp bảo vệ mạng máy tính và xây dựng hệ thống tổ chức an toàn, kiểm soát quyền truy cập, ngăn chặn tấn công hệ thống và đối phó với các cuộc tấn công botnet. Môn học cũng đề cập đến các vấn đề bảo vệ hệ thống mạng khỏi phần mềm độc hại, an ninh mạng trên các hệ điều hành Windows, Unix/Linux, bảo mật mạng truyền dẫn và các loại mạng như LAN, mạng không dây và mạng di động.",
            "query": "nhập môn bảo đảm và an ninh thông tin học những gì",
            "response":"",  
        },
        {
            "reference": "Môn Tiếng Anh chuyên ngành CNTT, được mã hóa là SPCH3723, tập trung vào việc cung cấp nền tảng từ vựng và khái niệm chuyên ngành máy tính. Mục tiêu của môn học là tạo điều kiện cho sinh viên tiếp thu kiến thức chuyên môn một cách hiệu quả thông qua các tài liệu chuyên ngành, đồng thời trau dồi kỹ năng trình bày báo cáo khoa học.",
            "query": "môn tiếng anh chuyên ngành CNTT có mục tiêu môn học là gì?",
            "response":"",
        },
        {
            "reference": "Môn Cấu trúc dữ liệu và giải thuật (IT003) giới thiệu vai trò quan trọng của giải thuật và tổ chức dữ liệu - những thành tố cơ bản trong mọi chương trình. Sinh viên sẽ khám phá và vận dụng các giải thuật và cấu trúc dữ liệu thường dùng để giải quyết các vấn đề trong lĩnh vực khoa học máy tính. Môn học này củng cố và nâng cao kỹ năng lập trình đã học ở các khóa trước.",
            "query": "Môn IT003 dùng để giải quyết các vấn đề trong lĩnh vực nào?",
            "response":"",
        },
        {
            "reference": "Môn Phát triển ứng dụng VR với mã số SE352 cung cấp cho sinh viên những kiến thức chuyên sâu về công nghệ Virtual Reality (VR) và hướng dẫn cách xây dựng ứng dụng VR dựa trên nền tảng Unity 3D. Thông qua việc học lập trình phần mềm VR, sinh viên có khả năng phát triển nhiều loại ứng dụng VR như trò chơi, mô hình kiến trúc, môi trường thực tế ảo giả lập.",
            "query": "Tôi muốn học công nghệ VR thì học môn gì",
            "response":"",  
        },
        {
            "reference": "Môn học CS313 là môn học về Khai thác dữ liệu và ứng dụng. Nội dung môn học tập trung vào việc cung cấp kiến thức và kỹ thuật khai thác dữ liệu để tìm ra tri thức quý báu từ các kho dữ liệu. Mối quan hệ giữa việc rút trích tri thức và quyết định, hoạch định chính sách sẽ được thảo luận thông qua nhiều ứng dụng thực tế. Trong môn học này, sinh viên sẽ được tìm hiểu về vai trò của khai thác dữ liệu, quá trình chuẩn bị dữ liệu, dự đoán/mô tả dữ liệu và các ứng dụng đi kèm, cùng với các vấn đề đang được quan tâm và giải quyết.",
            "query": "Nội dung của môn học CS313 là gì",
            "response":"",
        },
        {
            "reference":"Môn Đánh giá hiệu năng hệ thống mạng máy tính (mã môn NT531) cung cấp kiến thức toàn diện về đánh giá hiệu suất mạng. Nội dung chính bao gồm các mô hình đánh giá, đặc điểm của các kiến trúc mạng, phương pháp đo và khái niệm liên quan. Các công cụ hỗ trợ đánh giá hiệu suất cũng sẽ được giới thiệu. Môn học tập trung vào các kỹ thuật mô hình hóa phân tích nhằm dự đoán và xác nhận các tiêu chí thiết kế hệ thống máy tính và mạng. Các chủ đề chính bao gồm: ứng dụng mô hình hóa hiệu suất, mô hình hóa phân tích và mô phỏng, quá trình ngẫu nhiên, lý thuyết hàng cơ bản trong hệ thống máy tính và mạng, cũng như phương pháp giải quyết các mô hình phân tích hiệu suất.",
            "query": "Môn đánh giá hiệu năng hệ thống mạng máy tính có chủ đề chính gồm các phương pháp giải quyết các mô hình phân tích hiệu suất đúng không?",
            "response": "",
        },
        {
            "reference": "Môn IT008 có tên đầy đủ là Lập trình trực quan, cung cấp kiến thức và kỹ thuật lập trình bằng giao diện trực quan trên hệ điều hành Windows. Nội dung học tập bao gồm những phương pháp và quy trình tạo ứng dụng Windows, xử lý tin nhắn, sử dụng giao diện điều khiển, quản lý bộ nhớ, liên kết thư viện động và lập trình đa nhiệm.",
            "query": "Lập trình trực quan có mã môn học là gì?",
            "response":"",
        },
        {
            "reference": "Môn SE340 có tên gọi là Quản lý dự án công nghệ thông tin, trang bị cho sinh viên công nghệ thông tin chuyên ngành những kiến thức nền tảng trong một học kỳ để có thể triển khai, hoạch định và tổ chức công việc của người quản lý dự án dựa trên yêu cầu quản trị kỹ thuật. Nội dung môn học gồm: Chương 1 trình bày tổng quan về quản lý dự án, khung làm việc, định hướng phát triển hiện tại và tương lai. Chương 2 giới thiệu về quản trị phạm vi dự án, phương pháp chọn lựa dự án và mô tả tài liệu dự án trong giai đoạn khởi đầu. Chương 3 đào sâu về quản trị thời gian, kỹ thuật triển khai lập kế hoạch và ước lượng thực hiện dự án. Chương 4 tập trung vào chi phí dự án, kỹ thuật ước lượng và phân bổ ngân sách. Các chương tiếp theo sẽ cung cấp kiến thức và bước hỗ trợ nâng cao trong việc tổ chức nhân sự, đảm bảo chất lượng, kiểm soát rủi ro, triển khai mua sắm và tích hợp dự án.",
            "query": "Chương 1 của môn SE340 là gì?",
            "response":"",
        },
        {
            "reference": "Môn học CS116 về Lập trình Python cho Máy học cung cấp kiến thức và kỹ năng lập trình bằng ngôn ngữ Python, sử dụng các công cụ, thư viện và nền tảng tính toán hiện đại dựa trên Python để phát triển và áp dụng hiệu quả các phương pháp máy học.",
            "query": "Môn lập trình python cho máy học cung cấp kiến thức và kỹ năng lập trình bằng ngôn ngữ gì",
            "response":"",
        },
        {
            "reference": "Cử nhân ngành Kỹ thuật Phần mềm (Áp dụng từ khóa 18 - 2023) Hình thức đào tạo: Chính quy tập trung. Số tín chỉ đào tạo: 130. Thời gian đào tạo: 4 năm (8 học kỳ chính); 167",
            "query": "cử nhân ngành kỹ thuật phần mềm có thời gian đào tạo trong mấy học kỳ chính",
            "response":"",
        },
        {
            "reference": "Môn IS217: Môn học Kho dữ liệu và OLAP tập trung vào kiến thức nền tảng và nâng cao về kho dữ liệu, các kỹ thuật phân tích và thiết kế kho dữ liệu, mô hình dữ liệu đa chiều và ngôn ngữ truy vấn cơ sở dữ liệu đa chiều, phục vụ cho việc xây dựng các ứng dụng thực tế trong doanh nghiệp. Ngoài ra, môn học còn trang bị cho sinh viên các kỹ năng thiết kế và mô phỏng cơ sở dữ liệu dạng khối, phân tích dữ liệu đa chiều, khai phá dữ liệu, trích xuất, chuyển đổi và tải dữ liệu vào kho, sử dụng thành thạo các công cụ trí tuệ kinh doanh (BI) và ngôn ngữ truy vấn dữ liệu đa chiều.",
            "query":"Môn IS217 tập trung kiến thức nền tảng và nâng cao về những gì?",
            "response":"",
        },
        {
            "reference": "Môn học ""Giới thiệu ngành Mạng máy tính và Truyền thông dữ liệu"" (mã môn NT005) cung cấp cái nhìn tổng quan về ngành Công nghệ thông tin (CNTT), bao gồm cả những chuyên ngành chuyên sâu. Môn học giúp sinh viên hiểu rõ nội dung đào tạo và triển vọng nghề nghiệp trong ngành, nắm được các lĩnh vực và công việc có thể đảm nhiệm sau khi tốt nghiệp.",
            "query": "Môn NT005 học những gì?",
            "response":"",
        },
        {
            "reference": "Môn học Trình biên dịch có mã môn học là CE318. Tóm tắt nội dung môn học như sau: Môn học Trình biên dịch bao gồm việc nghiên cứu về nguyên tắc hoạt động của trình biên dịch, các kỹ thuật được sử dụng để thiết kế một trình biên dịch và các công cụ như Lex, Yacc để giúp việc cài đặt một trình biên dịch trở nên thuận tiện.",
            "query": "môn học nghiên cứu về nguyên tắc hoạt động của trình biên dịch là môn gì?",
            "response": "",
        },
        {
            "reference":"Môn học CE005 - Giới thiệu ngành Kỹ Thuật Máy tính, nhằm giúp sinh viên hiểu rõ về ngành học và định hướng nghề nghiệp, từ đó củng cố đam mê và xây dựng kế hoạch học tập phù hợp. Môn học này được thiết kế để cung cấp cái nhìn tổng quan về ngành Kỹ Thuật Máy Tính trong bối cảnh phát triển mạnh mẽ của ngành Công nghệ thông tin và Truyền thông, đặc biệt là công nghệ IoT. Ngoài ra, môn học cũng cung cấp thông tin về các nhóm ngành, yêu cầu và tương lai phát triển, giúp sinh viên nắm bắt cơ hội và xây dựng kế hoạch học tập đúng đắn.",
            "query": "CE005 là môn giới thiệu ngành gì",
            "response":"",
        },
        {
            "reference": "Môn học có tên mã là CS323 là môn học về hệ thống hỏi-đáp. Nội dung môn học tập trung vào kiến thức cơ bản về nghiên cứu Question Answering trong xử lý ngôn ngữ tự nhiên, bao gồm phân tích câu hỏi, phân tích tài liệu văn bản để xác định câu trả lời, mô hình hệ thống hỏi-đáp và phương pháp đánh giá hệ thống hỏi-đáp.",
            "query": "tôi muốn học về question answering thì nên học môn nào?",
            "response":"",
        },
        #--------------------
        {
            "reference": "Môn Các vấn đề chọn lọc trong Thị giác máy tính (CS420) là một môn học có nội dung linh hoạt, tập trung chủ yếu vào các chủ đề và vấn đề mới nhất trong lĩnh vực này. Môn học CS231 về Thị giác máy tính giới thiệu các kiến thức căn bản trong lĩnh vực này, bao gồm low-level computer vision và mid-level computer vision. Các chủ đề cụ thể bao gồm rút trích và khai thác thông tin trên ảnh, các loại đặc trưng thị giác cấp thấp và phương pháp biểu diễn đặc trưng thị giác cấp thấp, kĩ thuật so khớp ảnh, kĩ thuật phân đoạn ảnh và phương pháp theo vết (tracking).",
            "query": "Môn các vấn đề chọn lọc trong thị giác máy tính có mã môn là CS231 dạy những gì?",
            "response": "", 
        },
        {
            "reference": "Cử nhân ngành Kỹ thuật Phần mềm (Áp dụng từ khóa 18 - 2023) Hình thức đào tạo: Chính quy tập trung. Số tín chỉ đào tạo: 130. Thời gian đào tạo: 4 năm (8 học kỳ chính); 167. Cử nhân ngành Công nghệ Thông tin (Áp dụng từ Khoá 18 - 2023) ngành công nghệ thông tin việt nhật. Hình thức đào tạo: Chính quy tập trung. Số tín chỉ đào tạo: Tối thiểu 132 tín chỉ (bao gồm cả ngoại ngữ). Thời gian đào tạo: 04 năm (8 học kỳ chính). ",
            "query": "Cử nhân nghành kỹ thuật phần mềm cần 132 tín chỉ đào tạo đúng không?",
            "response": "",
        },
        {
            "reference": "Môn học CE407 - Đồ án chuyên ngành Hệ thống nhúng và Robot dành cho sinh viên học chuyên đề tốt nghiệp. Đồ án này giúp sinh viên phát triển kỹ năng thiết kế hệ thống nhúng và robot. Sau khi hoàn thành môn học, sinh viên sẽ có kiến thức tổng hợp về chuyên ngành hệ thống nhúng và robot, kỹ năng tìm hiểu, nghiên cứu và giải quyết bài toán trong lĩnh vực hệ thống nhúng, kỹ thuật máy tính, cũng như kỹ năng thuyết trình, giao tiếp và làm việc nhóm. Môn học cũng khuyến khích thái độ làm việc tích cực trong lĩnh vực hệ thống nhúng. Môn học ""Phát triển và vận hành game"" với mã môn học là SE327, cung cấp những kiến thức cơ bản về quy trình tạo ra và quản lý một trò chơi trực tuyến. Nội dung học tập bao gồm các thể loại game từ bình thường, hành động, chiến lược cho đến nhập vai trực tuyến nhiều người chơi độc lập hoặc trên nền tảng mạng xã hội.",
            "query": "Môn CE407 có nội dung là cung cấp những kiến thức cơ bản về quy trình tạo ra và quản lý một trò chơi trực tuyến đúng không?",
            "respone":"",
        },
        {
            "reference": "Môn Nhập môn mạng máy tính với mã IT005 cung cấp kiến thức cơ bản về các khái niệm như mạng máy tính, truyền dữ liệu, dịch vụ mạng và kỹ thuật mạng không dây. Môn học CS221 về Xử lý ngôn ngữ tự nhiên nhằm cung cấp cho sinh viên những kiến thức cơ bản về chuyên ngành này, bao gồm văn phạm phi ngữ cảnh CFG, văn phạm DCG, cách cài đặt và giải thích cơ chế xử lý văn phạm DCG trên Prolog, và FSA.",
            "query": "Môn Xử lý ngôn ngữ tự nhiên có mã môn là IT005 dạy những gì?",
            "response":"", 
        },
        {
            "reference": "Môn học CE411 là Chuyên đề hệ thống nhúng và robot. Nội dung môn học tập trung vào khả năng phân tích và thiết kế hệ thống nhúng hoặc robot cụ thể. Sinh viên sẽ được học về các lý thuyết liên quan đến board nhúng và robot, cũng như các qui trình và cách thực hiện để tạo ra sản phẩm nhúng thực tế, bao gồm cả phần cứng và phần mềm. Môn học Hệ thống thông tin kế toán (mã môn: IS232) giới thiệu kiến thức toàn diện về công tác kế toán. Nội dung môn học bao gồm: nguyên lý kế toán, các chu trình nghiệp vụ trong kế toán, cách thức tổ chức và xây dựng hệ thống thông tin kế toán, cũng như ứng dụng công nghệ thông tin vào các nghiệp vụ kế toán.",
            "query": "Môn hệ thống thông tin kế toán có mã môn học là CE411 có nội dung là gì?",
            "response":"",
        },
        {
            "reference": "Môn học Máy học có mã môn học là CS114. Tóm tắt nội dung môn học như sau: Môn học cung cấp kiến thức cơ bản về Máy học. Nội dung chính bao gồm: Giới thiệu tổng quan về máy học, bao gồm khái niệm, lịch sử và ứng dụng của Máy học, cùng với các công cụ, công nghệ và thách thức hiện nay. Các cách sử dụng máy học để giải quyết vấn đề, bao gồm các bài toán tiêu biểu như hồi quy, phân lớp, gom cụm và các phương pháp cơ bản để giải quyết. Môn học CS116 về Lập trình Python cho Máy học cung cấp kiến thức và kỹ năng lập trình bằng ngôn ngữ Python, sử dụng các công cụ, thư viện và nền tảng tính toán hiện đại dựa trên Python để phát triển và áp dụng hiệu quả các phương pháp máy học.",
            "query": "CS114 có tên môn học là lập trình python cho máy học có nội dung môn học là gì?",
            "response": "",
        },
        {
            "reference": "Môn học CS314 về Lập trình symbolic trong Trí tuệ nhân tạo giới thiệu về lập trình tính toán hình thức bằng ngôn ngữ Maple, giới thiệu về các lệnh thường dùng và các kiểu cấu trúc dữ liệu trong Maple, và ứng dụng lập trình tính toán trong thiết kế thuật giải heuristic và mạng tính toán trong Trí tuệ nhân tạo. Môn học Trí tuệ nhân tạo (Artificial Intelligence) được ký hiệu là IE229. Về nội dung, môn học cung cấp một bức tranh toàn diện về lĩnh vực trí tuệ nhân tạo, trình bày các vấn đề trong lĩnh vực này cùng với những phương pháp thường dùng để giải quyết. Môn học bao gồm các kiến thức cơ bản về thuật giải, thuật toán, các cách tiếp cận để tìm lời giải cho các bài toán cũng như các phương pháp tìm kiếm giải pháp nhanh (heuristic). Bên cạnh đó, môn học cũng giới thiệu tổng quan về học máy (machine learning), các mô hình học máy phổ biến (học có giám sát, học không giám sát, ...) và các kỹ thuật đánh giá mô hình học máy.",
            "query": "Môn trí tuệ nhân tạo có mã môn là CS314 dạy những gì?",
            "response":"",
        },
        {
            "reference": "Môn học Truy xuất thông tin với mã môn CS419 giới thiệu những nguyên lý cơ bản của lĩnh vực truy xuất thông tin, bao gồm: các mô hình truy xuất thông tin, các kỹ thuật lập chỉ mục, mô hình không gian véc-tơ và phương pháp đánh giá hiệu quả của các mô hình. Ngoài ra, sinh viên sẽ thực hiện một đồ án môn học để áp dụng những kiến thức đã học. Mục tiêu của môn học là cung cấp cho sinh viên kiến nền trong lĩnh vực truy xuất thông tin, giúp sinh viên có khả năng triển khai các dự án thực tế dựa trên kiến thức đã tiếp thu, dưới sự hướng dẫn của giảng viên. Môn Hệ truyền thông dữ liệu có ký hiệu là MSIS4523. Về nội dung, môn học này sẽ đề cập đến các loại mạng và giao thức mạng được ứng dụng trong việc truyền tải thông tin đa dạng ngày nay, bao gồm giọng nói, hình ảnh và dữ liệu thương mại. Bên cạnh đó, học viên sẽ được trang bị các thuật ngữ mạng và hiểu biết về cách vận hành của các thành phần trong hệ thống viễn thông.",
            "query": "môn truy xuất thông tin có nội dung môn học là về các loại mạng và giao thức mạng được ứng dụng trong việc truyền tải thông tin đúng không?",
            "response":""
        },
  
])

df.to_csv(r"C:\Users\leduc\OneDrive\Desktop\NLP\LLM-Agent\AI _solution\evalutation.csv")