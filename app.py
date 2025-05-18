#BInaray calculator
import streamlit as st

# Function to convert decimal to 8-bit binary
def to_binary(num):
    return format(num, "08b")

# Binary Number System Information
def binary_info():
    st.markdown("""
    ## 🔢 Understanding the Binary Number System  
    - **Binary** uses only two digits: **0 and 1**.
    - Each position represents a power of **2**.
    - **Example:** Converting **5** to binary:
      - 5 ÷ 2 = 2 remainder **1**
      - 2 ÷ 2 = 1 remainder **0**
      - 1 ÷ 2 = 0 remainder **1**  
      - **Binary of 5 = 101** (Read from bottom to top)
    """)

# Binary Chart Function
def binary_chart():
    st.write("### 🧮 Binary Conversion Chart (0-15)")
    chart_data = {i: to_binary(i) for i in range(16)}
    st.table(chart_data)

# Bitwise Operators Explanation
def bitwise_explanation():
    st.markdown("""
    ## ⚡ Bitwise Operators Explained
    - **AND (&):** Sets bits to **1** if both are **1**.
    - **OR (|):** Sets bits to **1** if at least one is **1**.
    - **XOR (^):** Sets bits to **1** if they are different.
    - **NOT (~):** Inverts bits (1 → 0, 0 → 1).
    - **Left Shift (<<):** Moves bits **left**, multiplying by **2^n**.
    - **Right Shift (>>):** Moves bits **right**, dividing by **2^n**.
    """)

# Streamlit UI
st.title("⚡ Binary & Bitwise Calculator")

# Display Binary Number System Knowledge
binary_info()
st.write("---")

# Display Binary Chart
binary_chart()
st.write("---")

bitwise_explanation()
st.write("---")

st.write("### 🛠 Enter two numbers to perform bitwise operations")

# User Inputs
num1 = st.number_input("Enter First Number", value=5, step=1)
num2 = st.number_input("Enter Second Number", value=3, step=1)

# Display Binary Representations
st.write(f"🟢 **Binary of {num1}:** `{to_binary(num1)}`")
st.write(f"🟢 **Binary of {num2}:** `{to_binary(num2)}`")

st.write("---")

# Bitwise Operation
st.write("## 🔢 Bitwise Operations with Explanation")
st.write(f"✅ **AND (&) →** `{num1 & num2}` (Binary: `{to_binary(num1 & num2)}`) → Common bits remain 1")
st.write(f"✅ **OR (|) →** `{num1 | num2}` (Binary: `{to_binary(num1 | num2)}`) → Any bit being 1 results in 1")
st.write(f"✅ **XOR (^) →** `{num1 ^ num2}` (Binary: `{to_binary(num1 ^ num2)}`) → Different bits become 1")
st.write(f"✅ **NOT (~num1) →** `{~num1}` (Binary: `{to_binary(~num1 & 0xFF)}`) → Flips all bits (8-bit mask applied)")
st.write(f"✅ **Left Shift (num1 << 2) →** `{num1 << 2}` (Binary: `{to_binary(num1 << 2)}`) → Multiplies by 4")
st.write(f"✅ **Right Shift (num1 >> 2) →** `{num1 >> 2}` (Binary: `{to_binary(num1 >> 2)}`) → Divides by 4")

st.write("---")

st.success("💡 Try entering different numbers to see real-time binary calculations!")
