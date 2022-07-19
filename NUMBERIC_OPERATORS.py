"""
==== Các kiểu dữ liệu số

int		: kiểu số nguyên kiểu này có kích thước không giới hạn (python 2 thì bị hạn chế).
float	: kiểu số thực. Kiểu này ngoài kiể viết bình thường ra thì nó cũng có thể được hiển thị dưới dạng số mũ E (VD: 2.5e2 = 250).
complex	: kiểu số phức đây là kiểu dữ liệu rất ít khi được sử dụng

==== Thao tác với số

del del avariableName
del avariableName1, avariableName2,..., avariableName3

Toán Tử	|		Ví Dụ		|	Chú Thích
		|					|
	+	|	a + b  // 15	|	Phép cộng.
	-	|	a - b // -5		|	Phép trừ.
	*	|	a * b // 50		|	Phép nhân.
	/	|	a / b // 0.5	|	Phép chia.
	%	|	a % b // 5		|	Phép chia lấy dư.

==== Các dạng toán tử

Toán tử số học - Arithmetic Operators
Toán tử quan hệ - Comparison (Relational) Operators
Toán tử gán - Assignment Operators.
Toán tử logic - Logical Operators.
Toán tử Biwter - Bitwise Operators.
Toán tử khai thác - Membership Operators.
Toán tử xác thực - Indentity Operators.

==== Chi tiết các toán tử
Toán tử số học - Arithmetic Operators
VD: a = 5 và b = 7

Toán tử		Mô Tả									Ví Dụ
	+		Toán tử cộng các giá trị lại với nhau	a + b = 12
	-		Toán tử trừ các giá trị lại với nhau	a - b = -2
	*		Toán tử nhân các giá trị lại với nhau	a * b = 42
	/		Toán tử chia các giá trị cho nhau		a / b = 0.7142857142857143
	%		Toán tử chia lấy phần dư				a % b = 5
	**		Toán tử mũ. a**b = a^b					a ** b = 78125
	//		Toán tử chia làm tròn xuống				a // b = 0, 0,57 => 0, 0.9 => 0, -07 => -1, -0.1 => -1
			(chia lấy phần nguyên)

============================
Toán tử quan hệ - Comparison (Relational) Operators
Dạng toán dùng để so sánh các giá trị và giá trị trả về là True / False
VD a = 5 và b = 7

	Toán tử	|				Chú Thích					|	Ví Dụ
			|											|
	==		|	So sánh giá trị bằng nhàu không			|	a == b	//False
	!=		|	So sánh giá trị khác nhau không			|	a != b 	//True
	<		|	So sánh giá trị nhỏ hơn không			|	a < b 	//True
	>		|	So sánh giá trị lớn hơn không			|	a > b 	//False	
	<=		|	So sánh giá trị nhỏ hơn hoặc bằng không	|	a <= b 	//True
	>=		|	So sánh giá trị lớn hơn hoặc bằng không	|	a>= b 	//False

============================
Toán tử gán - Assignment Operators
Dạng toàn dùng để gán giá trị cho đối tượng
VD a = 5

	Toán Tử	|						Chú thích					|		Ví Dụ
	=		|	Gán giá trị của một đối tượng cho một đối tượng	|	c = a	(c sẽ có giá trị = 5)
	+=		|	Cộng rồi gắn giá trị cho đối tượng				|	c += a	(tương đương c = c + a)
	-=		|	Trừ rồi gắn giá trị cho đối tượng				|	c -= a	(tương đương c = c - a)
	*=		|	Trừ rồi gắn giá trị cho đối tượng				|	c *= a	(tương đương c = c * a)
	/=		|	Chia rồi gắn giá trị cho đối tượng				|	c /= a	(tương đương c = c / a)
	%=		|	Chia hết rồi gắn giá trị cho đối tượng			|	c %= a	(tương đương c = c % a)
	**=		|	Lũy thừa rồi gắn giá trị cho đối tượng			|	c **= a	(tương đương c = c ** a)
	//=		|	Chia làm tròn rồi gắn giá trị cho đối tượng		|	c //= a	(tương đương c = c // a)

============================
Toán tử logic - Logical Operators
	Toán Tử		|						Chú Thích
		and		|	2 vế True là True. 1 trong 2 vế False là False.
		or		|	1 trong 2 vế True là True. 2 vế False là False.
		not		|	Dạng phủ định, biểu thức là True trả về False và ngược lại.

============================
Toán tử Biwter - Bitwise Operators
Toán tử này thực hiện trên các bit của các giá trị, rất ít khi sử dụng
a = 12 và b = 15 chuyển sang nhị phân a = 00001100 và b = 00001111

	Toán Tử		| 	Chú thích			|		Ví Dụ
		&		|	Phần giao nhau - sao chép bit 1 giống nhau của 2 số hạng, nếu khác trả về 0		|	(a & b) = 12	(00001100)
		|		|	Kết hợp cả 2 - sao chép bit 1 tồn tại ở 2 số hạng								|	(a | b) = 15	(00001111)
		^		|	loại bỏ phần giao - sao chép bit 1 nếu bit đó chỉ tồn tại ở 1 trong 2 số hạng	|	(a ^ b) = 3		(00000011) 
		~		|	Đảo ngôi, bit 1 thành 0, bit 0 thành 1											|	(~a) = -12		(11110011)
		>>		|	Dịch phải số bit được định nghĩa bởi toán hàng phải								|	a>>2 = 2		(00000011) (số bit a dịch sang phải 2 đơn vị)
		<<		|	Dịch trái số bit được định nghĩa bởi toán hàng phải								|	a<<2 = 48		(00110000)

============================
Toán tử khai thác - Membership Operators.
thường được dùng để kiểm tra xem 1 đối số có nằm trong 1 tập hợp đối số hay không (list)

VD: a = 4, b = [1,5,7,6,9]

	Toán Tử	|										Chú Thích							|		Ví Dụ
	in		|	Nếu 1 đối số thuộc một tập đối số nó sẽ trả về True và ngược lại		|	a in b		//False
	not in	|	Nếu 1 đối số không thuộc một tập đối số nó sẽ trả về True và ngược lại	|	a not in b	//True

============================
Toán tử xác thực - Indentity Operators
Dùng để xác thực hai giá trị xem nó có bằng nhau hay không

VD: a = 4, b =5

	Toán Tử	|							Chú Thích					|		Ví Dụ
	is		|	Toán tử này sẽ trả về True nếu a == b và ngược lại	|	a is b		//False
	not is	|	Toán tử này sẽ trả về True nếu a != b và ngược lại	|	a is not b	//True

"""