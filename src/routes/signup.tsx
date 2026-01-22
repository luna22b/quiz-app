import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import axios from "axios";

export const Route = createFileRoute("/signup")({
  component: Signup,
});

function Signup() {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [confirmPassword, setConfirmPassword] = useState<string>("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // checks if the password is the same as the confirmation
    if (confirmPassword != password) {
      alert("Passwords don't match!");
      return;
    }

    type Signup = {
      username: string;
      password: string;
      email: string;
    };

    const data: Signup = {
      username: username,
      password: password,
      email: email,
    };

    // send user data to the backend
    axios
      .post("http://localhost:5713/signup", data)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });

    console.log({ email, password });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="bg-amber-100"
          placeholder="username"
          required
        />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="bg-amber-100"
          placeholder="email"
          required
        />

        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="password"
          className="bg-amber-100"
          required
        />

        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          placeholder="confirm password"
          className="bg-amber-100"
          required
        />

        <button type="submit">Signup</button>
      </form>
    </div>
  );
}
