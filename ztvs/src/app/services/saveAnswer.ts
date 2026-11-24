
const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

// test with hello()
export async function saveAnswer(answ:string){
console.log(API_URL);
  const response = await fetch(`${API_URL}/api/hello`);

  if(!response.ok) {
    console.log(response.text+response.status.toString());
  }
  else{
    console.log(answ);
  }

  //return response.json();
}