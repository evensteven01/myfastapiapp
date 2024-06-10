async function fetchData() {
  const response = await fetch('/api/time_service/current_time');
  const data = await response.json();
  console.log(data);
  document.getElementById("resultData").innerHTML = data.current_time;
}