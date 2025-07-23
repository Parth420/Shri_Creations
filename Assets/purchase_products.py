import json

products = [
  {
    "id": 1,
    "name": "Ear Chain 1",
    "price": 1000,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%201.jpg",
    "description": ""
  },
  {
    "id": 2,
    "name": "Ear Chain 2",
    "price": 2000,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%202.jpg",
    "description": ""
  },
  {
    "id": 3,
    "name": "Ear Chain 3",
    "price": 1400,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%203.jpg",
    "description": ""
  },
  {
    "id": 5,
    "name": "Ear Chain 5",
    "price": 1600,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%204.jpg",
    "description": ""
  },
  {
    "id": 6,
    "name": "Ear Chain 6",
    "price": 1200,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%205.jpg",
    "description": ""
  },
  {
    "id": 7,
    "name": "Ear Chain 7",
    "price": 1600,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%206.jpg",
    "description": ""
  },
  {
    "id": 9,
    "name": "Ear Chain 9",
    "price": 1200,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%207.jpg",
    "description": ""
  },
  {
    "id": 10,
    "name": "Ear Chain 10",
    "price": 2000,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%208.jpg",
    "description": ""
  },
  {
    "id": 12,
    "name": "Ear Chain 12",
    "price": 800,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%209.jpg",
    "description": ""
  },
  {
    "id": 13,
    "name": "Ear Chain 13",
    "price": 1400,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2010.jpg",
    "description": ""
  },
  {
    "id": 15,
    "name": "Ear Chain 15",
    "price": 2000,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2011.jpg",
    "description": ""
  },
  {
    "id": 16,
    "name": "Ear Chain 16",
    "price": 600,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2012.jpg",
    "description": ""
  },
  {
    "id": 17,
    "name": "Ear Chain 17",
    "price": 1500,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2013.jpg",
    "description": ""
  },
  {
    "id": 18,
    "name": "Ear Chain 18",
    "price": 3500,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2014.jpg",
    "description": ""
  },
  {
    "id": 19,
    "name": "Ear Chain 19",
    "price": 2000,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2015.jpg",
    "description": ""
  },
  {
    "id": 32,
    "name": "Ear Chain 20",
    "price": 1700,
    "category": "earchain",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Chain/Ear%20Chain%2016.jpg",
    "description": ""
  },
  {
    "id": 20,
    "name": "Ear Cuffs 1",
    "price": 1000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%201.jpg",
    "description": ""
  },
  {
    "id": 21,
    "name": "Ear Cuffs 2",
    "price": 1000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%202.jpg",
    "description": ""
  },
  {
    "id": 22,
    "name": "Ear Cuffs 3",
    "price": 5000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%203.jpg",   
    "description": ""
  },
  {
    "id": 23,
    "name": "Ear Cuffs 4",
    "price": 4000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%204.jpg",   
    "description": ""
  },
  {
    "id": 24,
    "name": "Ear Cuffs 5",
    "price": 1000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%205.jpg",   
    "description": ""
  },
  {
    "id": 25,
    "name": "Ear Cuffs 6",
    "price": 1000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%206.jpg",   
    "description": ""
  },
  {
    "id": 26,
    "name": "Ear Cuffs 7",
    "price": 5000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%207.jpg",   
    "description": ""
  },
  {
    "id": 27,
    "name": "Ear Cuffs 8",
    "price": 700,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%208.jpg",   
    "description": ""
  },
  {
    "id": 28,
    "name": "Ear Cuffs 9",
    "price": 2700,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%209.jpg",   
    "description": ""
  },
  {
    "id": 29,
    "name": "Ear Cuffs 10",
    "price": 1000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%2010.jpg",  
    "description": ""
  },
  {
    "id": 30,
    "name": "Ear Cuffs 11",
    "price": 5000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%2011.jpg",  
    "description": ""
  },
  {
    "id": 31,
    "name": "Ear Cuffs 12",
    "price": 2300,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%2012.jpg",  
    "description": ""
  },
  {
    "id": 4,
    "name": "Ear Cuffs 13",
    "price": 1000,
    "category": "earcuffs",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Ear%20Cuffs/Ear%20Cuffs%2013.jpg",  
    "description": ""
  },
  {
    "id": 33,
    "name": "Hair Accessories 1",
    "price": 1000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%201.jpg",   
    "description": ""
  },
  {
    "id": 34,
    "name": "Hair Accessories 2",
    "price": 2000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%202.jpg",   
    "description": ""
  },
  {
    "id": 35,
    "name": "Hair Accessories 3",
    "price": 2000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%203.jpg",   
    "description": ""
  },
  {
    "id": 36,
    "name": "Hair Accessories 4",
    "price": {
      "<built-in function min>": 800,
      "<built-in function max>": 1000
    },
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%204.jpg",   
    "description": ""
  },
  {
    "id": 37,
    "name": "Hair Accessories 5",
    "price": 1000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%205.jpg",   
    "description": ""
  },
  {
    "id": 38,
    "name": "Hair Accessories 6",
    "price": 2000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%206.jpg",   
    "description": ""
  },
  {
    "id": 39,
    "name": "Hair Accessories 7",
    "price": 1000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%207.jpg",   
    "description": ""
  },
  {
    "id": 40,
    "name": "Hair Accessories 8",
    "price": 500,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%208.jpg",   
    "description": ""
  },
  {
    "id": 41,
    "name": "Hair Accessories 9",
    "price": 700,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%209.jpg",   
    "description": ""
  },
  {
    "id": 42,
    "name": "Hair Accessories 10",
    "price": 2000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2010.jpg",  
    "description": ""
  },
  {
    "id": 43,
    "name": "Hair Accessories 11",
    "price": 600,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2011.jpg",  
    "description": ""
  },
  {
    "id": 44,
    "name": "Hair Accessories 12",
    "price": 1200,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2012.jpg",  
    "description": ""
  },
  {
    "id": 45,
    "name": "Hair Accessories 13",
    "price": 700,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2013.jpg",  
    "description": ""
  },
  {
    "id": 46,
    "name": "Hair Accessories 14",
    "price": 3000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2014.jpg",  
    "description": ""
  },
  {
    "id": 47,
    "name": "Hair Accessories 15",
    "price": 3500,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2015.jpg",  
    "description": ""
  },
  {
    "id": 48,
    "name": "Hair Accessories 16",
    "price": {
      "<built-in function min>": 350,
      "<built-in function max>": 1000
    },
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2016.jpg",  
    "description": ""
  },
  {
    "id": 49,
    "name": "Hair Accessories 17",
    "price": 5000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2017.jpg",  
    "description": ""
  },
  {
    "id": 50,
    "name": "Hair Accessories 18",
    "price": 1800,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2018.jpg",  
    "description": ""
  },
  {
    "id": 96,
    "name": "Hair Accessories 19",
    "price": 1500,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2019.jpg",  
    "description": ""
  },
  {
    "id": 75,
    "name": "Hair Accessories 20",
    "price": 1500,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2020.jpg",  
    "description": ""
  },
  {
    "id": 89,
    "name": "Hair Accessories 21",
    "price": 500,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2021.jpg",  
    "description": ""
  },
  {
    "id": 90,
    "name": "Hair Accessories 22",
    "price": 300,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2022.jpg",  
    "description": ""
  },
  {
    "id": 91,
    "name": "Hair Accessories 23",
    "price": 2000,
    "category": "hair",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hair%20Accessories/Hair%2023.jpg",  
    "description": ""
  },
  {
    "id": 51,
    "name": "Hand Accessories 1",
    "price": 5000,
    "category": "hand",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hand%20Accessories/Hand%201.jpg",   
    "description": ""
  },
  {
    "id": 52,
    "name": "Hand Accessories 2",
    "price": 5000,
    "category": "hand",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hand%20Accessories/Hand%202.jpg",   
    "description": ""
  },
  {
    "id": 53,
    "name": "Hand Accessories 3",
    "price": 1000,
    "category": "hand",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hand%20Accessories/Hand%203.jpg",   
    "description": ""
  },
  {
    "id": 54,
    "name": "Hand Accessories 4",
    "price": 700,
    "category": "hand",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hand%20Accessories/Hand%204.jpg",   
    "description": ""
  },
  {
    "id": 55,
    "name": "Hand Accessories 5",
    "price": 1000,
    "category": "hand",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hand%20Accessories/Hand%205.jpg",   
    "description": ""
  },
  {
    "id": 56,
    "name": "Hand Accessories 6",
    "price": 6000,
    "category": "hand",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Hand%20Accessories/Hand%206.jpg",   
    "description": ""
  },
  {
    "id": 55,
    "name": "Maangtikka 1",
    "price": {
      "<built-in function min>": 300,
      "<built-in function max>": 800
    },
    "category": "maangtikka",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Maangtikka%201.jpg",     
    "description": ""
  },
  {
    "id": 56,
    "name": "Maangtikka 2",
    "price": {
      "<built-in function min>": 300,
      "<built-in function max>": 800
    },
    "category": "maangtikka",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Maangtikka%202.jpg",     
    "description": ""
  },
  {
    "id": 57,
    "name": "Maangtikka 3",
    "price": {
      "<built-in function min>": 300,
      "<built-in function max>": 800
    },
    "category": "maangtikka",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Maangtikka%203.jpg",     
    "description": ""
  },
  {
    "id": 58,
    "name": "Maangtikka 4",
    "price": {
      "<built-in function min>": 200,
      "<built-in function max>": 1000
    },
    "category": "maangtikka",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Maangtikka%204.jpg",     
    "description": ""
  },
  {
    "id": 60,
    "name": "Maangtikka 6",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 1400
    },
    "category": "maangtikka",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Maangtikka%205.jpg",     
    "description": ""
  },
  {
    "id": 61,
    "name": "Maangtikka 7",
    "price": {
      "<built-in function min>": 350,
      "<built-in function max>": 1000
    },
    "category": "maangtikka",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Maangtikka%206.jpg",     
    "description": ""
  },
  {
    "id": 62,
    "name": "Nath 1",
    "price": 500,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%201.jpg",
    "description": ""
  },
  {
    "id": 63,
    "name": "Nath 2",
    "price": 800,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%202.jpg",
    "description": ""
  },
  {
    "id": 64,
    "name": "Nath 3",
    "price": 350,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%203.jpg",
    "description": ""
  },
  {
    "id": 65,
    "name": "Nath 4",
    "price": {
      "<built-in function min>": 400,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%204.jpg",
    "description": ""
  },
  {
    "id": 66,
    "name": "Nath 5",
    "price": {
      "<built-in function min>": 350,
      "<built-in function max>": 800
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%205.jpg",
    "description": ""
  },
  {
    "id": 67,
    "name": "Nath 6",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%206.jpg",
    "description": ""
  },
  {
    "id": 68,
    "name": "Nath 7",
    "price": 500,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%207.jpg",
    "description": ""
  },
  {
    "id": 69,
    "name": "Nath 8",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 600
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%208.jpg",
    "description": ""
  },
  {
    "id": 70,
    "name": "Nath 9",
    "price": {
      "<built-in function min>": 250,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%209.jpg",
    "description": ""
  },
  {
    "id": 71,
    "name": "Nath 10",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2010.jpg",
    "description": ""
  },
  {
    "id": 72,
    "name": "Nath 11",
    "price": {
      "<built-in function min>": 300,
      "<built-in function max>": 600
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2011.jpg",
    "description": ""
  },
  {
    "id": 73,
    "name": "Nath 12",
    "price": {
      "<built-in function min>": 150,
      "<built-in function max>": 400
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2012.jpg",
    "description": ""
  },
  {
    "id": 74,
    "name": "Nath 13",
    "price": {
      "<built-in function min>": 350,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2013.jpg",
    "description": ""
  },
  {
    "id": 76,
    "name": "Nath 15",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2014.jpg",
    "description": ""
  },
  {
    "id": 77,
    "name": "Nath 16",
    "price": 700,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2015.jpg",
    "description": ""
  },
  {
    "id": 78,
    "name": "Nath 17",
    "price": {
      "<built-in function min>": 300,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2016.jpg",
    "description": ""
  },
  {
    "id": 79,
    "name": "Nath 18",
    "price": 800,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2017.jpg",
    "description": ""
  },
  {
    "id": 80,
    "name": "Nath 19",
    "price": 700,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2018.jpg",
    "description": ""
  },
  {
    "id": 81,
    "name": "Nath 20",
    "price": 800,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2019.jpg",
    "description": ""
  },
  {
    "id": 82,
    "name": "Nath 21",
    "price": 800,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2020.jpg",
    "description": ""
  },
  {
    "id": 83,
    "name": "Nath 22",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2021.jpg",
    "description": ""
  },
  {
    "id": 84,
    "name": "Nath 23",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 800
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2022.jpg",
    "description": ""
  },
  {
    "id": 85,
    "name": "Nath 24",
    "price": 350,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2023.jpg",
    "description": ""
  },
  {
    "id": 86,
    "name": "Nath 25",
    "price": {
      "<built-in function min>": 600,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2024.jpg",
    "description": ""
  },
  {
    "id": 87,
    "name": "Nath 26",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2025.jpg",
    "description": ""
  },
  {
    "id": 88,
    "name": "Nath 27",
    "price": {
      "<built-in function min>": 400,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2026.jpg",
    "description": ""
  },
  {
    "id": 91,
    "name": "Nath 30",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 1000
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2027.jpg",
    "description": ""
  },
  {
    "id": 92,
    "name": "Nath 31",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2028.jpg",
    "description": ""
  },
  {
    "id": 93,
    "name": "Nath 32",
    "price": 500,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2029.jpg",
    "description": ""
  },
  {
    "id": 94,
    "name": "Nath 33",
    "price": {
      "<built-in function min>": 400,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2030.jpg",
    "description": ""
  },
  {
    "id": 95,
    "name": "Nath 34",
    "price": 150,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2031.jpg",
    "description": ""
  },
  {
    "id": 97,
    "name": "Nath 36",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2032.jpg",
    "description": ""
  },
  {
    "id": 98,
    "name": "Nath 37",
    "price": {
      "<built-in function min>": 600,
      "<built-in function max>": 800
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2033.jpg",
    "description": ""
  },
  {
    "id": 99,
    "name": "Nath 38",
    "price": {
      "<built-in function min>": 600,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2034.jpg",
    "description": ""
  },
  {
    "id": 100,
    "name": "Nath 39",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2035.jpg",
    "description": ""
  },
  {
    "id": 101,
    "name": "Nath 40",
    "price": {
      "<built-in function min>": 400,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2036.jpg",
    "description": ""
  },
  {
    "id": 102,
    "name": "Nath 41",
    "price": 350,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2037.jpg",
    "description": ""
  },
  {
    "id": 103,
    "name": "Nath 42",
    "price": {
      "<built-in function min>": 300,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2038.jpg",
    "description": ""
  },
  {
    "id": 104,
    "name": "Nath 43",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2039.jpg",
    "description": ""
  },
  {
    "id": 105,
    "name": "Nath 44",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2040.jpg",
    "description": ""
  },
  {
    "id": 106,
    "name": "Nath 45",
    "price": 380,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2041.jpg",
    "description": ""
  },
  {
    "id": 107,
    "name": "Nath 46",
    "price": {
      "<built-in function min>": 400,
      "<built-in function max>": 500
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2042.jpg",
    "description": ""
  },
  {
    "id": 108,
    "name": "Nath 47",
    "price": {
      "<built-in function min>": 500,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2043.jpg",
    "description": ""
  },
  {
    "id": 109,
    "name": "Nath 48",
    "price": {
      "<built-in function min>": 600,
      "<built-in function max>": 700
    },
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2044.jpg",
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2044.jpg",
    "description": ""
  },
  {
    "id": 14,
    "name": "Nath 49",
    "price": 600,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2045.jpg",
    "description": ""
  },
  {
    "id": 11,
    "name": "Nath 50",
    "price": 700,
    "category": "nath",
    "image": "https://raw.githubusercontent.com/Parth420/Shri_Creations/98cbd86b61ffd6beb4a0f5d2b61bed2bc69543b0/Jewellery_Pics/Purchase/Maangtikka/Nath%2046.jpg",
    "description": ""
  }
]