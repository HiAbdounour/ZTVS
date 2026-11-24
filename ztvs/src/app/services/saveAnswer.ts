
const API_URL = process.env.NEXT_PUBLIC_API_URL;

// test with hello()
export async function saveAnswer(answ:string){
  const response = await fetch(`${API_URL}/api/hello`);

  if(!response.ok) {
    throw new Error("Erreur API");
  }
  else{
    console.log(answ);
  }

  //return response.json();
}