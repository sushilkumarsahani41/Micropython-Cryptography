<h1 align="center">Micropython-Cryptogrtapy Library</h1>

<p align="justify"> A well-designed and efficient Micropython Cryptography Library is an invaluable asset for securing IoT projects in today's data-driven world. By implementing powerful cryptographic algorithms, safeguarding keys, and promoting community involvement, your library can become a catalyst for creating robust, secure, and privacy-centric IoT applications.
<br>
Remember, the proactive approach of fortifying your IoT devices with the Micropython Cryptography Library can make all the difference between vulnerable applications and resilient systems capable of withstanding the challenges posed by the ever-evolving digital landscape. Empower your IoT projects with the power of security today!
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## 🧐 About <a name = "about"></a>

In a digitally interconnected world, where Internet of Things (IoT) devices play an ever-expanding role in our lives, ensuring data security is paramount. Micropython, a lightweight implementation of Python for microcontrollers, provides an excellent platform for developing IoT applications. To fortify these applications against potential threats, a robust and efficient Micropython Cryptography Library is indispensable. In this comprehensive guide, we will explore the significance of cryptographic techniques, the advantages of using Micropython, and the step-by-step process of creating a powerful and secure Cryptography Library tailored for IoT devices.

## 🏁 Getting Started <a name = "getting_started"></a>

Follow these steps to integrate the Micropython Cryptography Library into your IoT project:

### Step 1: Prerequisites

Ensure you have the following prerequisites installed:

- Micropython (version XYZ or higher)
- Microcontroller SDK (if required for your hardware)

### Step 2: Installation

1. Clone this repository to your local machine:

- git clone https://github.com/sushilkumarsahani41/Micropython-Cryptography.git

2. Copy the crypt.py to IoT Device Such as ESP32 or any Micropython Device

- Here Your Installtion is Done 


## 🎈 Usage <a name="usage"></a>

```python
from crypt import crypt

#to Generate Key
import uos 
key = uos.urandom(16) # it will generate an 128 bits AES Key

# or You Can Manually Add it
key = b'1234567890123456'

#  init crypt lib
c = crypt(key)

# To Encrypt Plain Text
plain_text = "Hello World"
encrypted_text = c.encrypt(plain_text)

# To Decrypt Encrypted text 
decrypted_text = c.decrypt(encrypted_text) # For Decryption text must be in a form of bytes 

```
# Thank You 

# Happy Coding


