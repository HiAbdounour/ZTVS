
const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

// test with hello()
export async function saveAnswer(answ:string){

    const response = await fetch(`${API_URL}/api/vote`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ "answer":answ })
    });

    if (!response.ok) {
        alert(`Une erreur a eu lieu : Erreur ${response.status}`);
    }
    else {
        console.log(answ);
    }

}