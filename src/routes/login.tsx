import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import axios from "axios";

export const Route = createFileRoute("/login")({
  component: Login,
});

function Login() {
  const [identifier, setIdentifier] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    console.log({ identifier, password });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={identifier}
          onChange={(e) => setIdentifier(e.target.value)}
          className="bg-amber-100"
          placeholder="email or username"
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

        <button type="submit">Login</button>
      </form>
    </div>
  );
}
