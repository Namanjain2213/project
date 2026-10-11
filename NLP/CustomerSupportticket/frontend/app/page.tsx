
"use client";

import { useState } from "react";

type PredictionResponse = {
  input_text: string;
  predicted_label: number;
  predicted_intent: string;
};

export default function Home() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handlePredict() {
    const text = message.trim();

    if (!text) {
      setError("Please enter a customer message.");
      setResult(null);
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          typeof data.detail === "string"
            ? data.detail
            : "Unable to predict the intent. Please try again."
        );
      }

      setResult(data as PredictionResponse);
    } catch {
      setError(
        "Could not connect to the API. Check that your FastAPI backend is running."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 px-4 py-12 text-white sm:px-6">
      <div className="mx-auto max-w-3xl">
        <header className="mb-10 text-center">
          <p className="mb-3 text-sm font-semibold uppercase tracking-[0.25em] text-cyan-400">
            AI-Powered NLP Project
          </p>

          <h1 className="text-3xl font-bold tracking-tight sm:text-5xl">
            Customer Support
            <span className="block text-cyan-400">
              Intent Classifier
            </span>
          </h1>

          <p className="mx-auto mt-4 max-w-xl text-slate-300">
            Enter a banking customer message and let the trained NLP model
            identify its intent.
          </p>
        </header>

        <section className="rounded-2xl border border-slate-700 bg-slate-900 p-5 shadow-2xl sm:p-8">
          <label
            htmlFor="customer-message"
            className="mb-3 block text-sm font-medium text-slate-200"
          >
            Customer message
          </label>

          <textarea
            id="customer-message"
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            placeholder="Example: My card has not arrived yet..."
            maxLength={2000}
            rows={5}
            className="w-full resize-y rounded-xl border border-slate-600 bg-slate-950 p-4 text-white outline-none transition placeholder:text-slate-500 focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20"
          />

          <div className="mt-2 text-right text-xs text-slate-400">
            {message.length}/2000 characters
          </div>

          <button
            type="button"
            onClick={handlePredict}
            disabled={loading}
            className="mt-5 w-full rounded-xl bg-cyan-500 px-5 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Analyzing message..." : "Predict Intent"}
          </button>

          {error && (
            <div
              role="alert"
              className="mt-5 rounded-xl border border-red-500/30 bg-red-500/10 p-4 text-sm text-red-300"
            >
              {error}
            </div>
          )}

          {result && (
            <div
              aria-live="polite"
              className="mt-6 rounded-xl border border-emerald-500/30 bg-emerald-500/10 p-5"
            >
              <p className="text-sm font-medium text-emerald-300">
                Predicted intent
              </p>

              <h2 className="mt-2 break-words text-2xl font-bold text-white">
                {result.predicted_intent.replaceAll("_", " ")}
              </h2>

              <p className="mt-2 text-sm text-slate-300">
                Label ID: {result.predicted_label}
              </p>

              <div className="mt-4 border-t border-emerald-500/20 pt-4">
                <p className="text-xs uppercase tracking-wider text-slate-400">
                  Analyzed message
                </p>
                <p className="mt-2 break-words text-sm text-slate-200">
                  {result.input_text}
                </p>
              </div>
            </div>
          )}
        </section>

        <footer className="mt-8 text-center text-sm text-slate-500">
          Powered by TF-IDF and Linear SVM · Banking77 dataset
        </footer>
      </div>
    </main>
  );
}
