text = "X-DSPAM-Confidence:    0.8475";
num=text.find('0');
num1=text[num:];
num2=float(num1);
print(num2);
