/*
 * Quantyze browser-side helpers.
 *
 * This file provides lightweight API accessors for optional browser UI work
 * that consumes the Flask endpoints exposed by server.py.
 */

class QuantyzeClient {
  /**
   * Create a client for the Quantyze API.
   *
   * @param {string} baseUrl - API host prefix such as "http://127.0.0.1:9000".
   */
  constructor(baseUrl = "") {
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  /**
   * Fetch JSON from one Quantyze API endpoint.
   *
   * @param {string} path - Endpoint path beginning with "/api/".
   * @param {Object} params - Query parameters for the request.
   * @returns {Promise<Object>} Parsed response body.
   */
  async get(path, params = {}) {
    const url = new URL(this.baseUrl + path, window.location.origin);
    for (const [key, value] of Object.entries(params)) {
      if (value !== undefined && value !== null) {
        url.searchParams.set(key, String(value));
      }
    }

    const response = await fetch(url.toString());
    if (!response.ok) {
      throw new Error(`Quantyze API request failed: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  health() {
    return this.get("/api/health");
  }

  bookSummary() {
    return this.get("/api/book/summary");
  }

  bookDepth(levels = 10) {
    return this.get("/api/book/depth", { levels });
  }

  metrics() {
    return this.get("/api/metrics");
  }

  trades(limit = 200, offset = 0) {
    return this.get("/api/trades", { limit, offset });
  }

  executionLog(limit = 200, offset = 0) {
    return this.get("/api/execution-log", { limit, offset });
  }

  openOrders() {
    return this.get("/api/orders/open");
  }
}

/**
 * Build a compact UI-facing snapshot from summary and metrics payloads.
 *
 * @param {Object} bookSummary - Response from /api/book/summary.
 * @param {Object} metrics - Response from /api/metrics.
 * @returns {Object} Flattened browser-friendly summary.
 */
function buildDashboardSnapshot(bookSummary, metrics) {
  return {
    bestBid: bookSummary.best_bid,
    bestAsk: bookSummary.best_ask,
    spread: bookSummary.spread,
    midPrice: bookSummary.mid_price,
    currentPnl: bookSummary.agent ? bookSummary.agent.current_pnl : null,
    totalFilled: metrics.total_filled,
    fillCount: metrics.fill_count,
    cancelCount: metrics.cancel_count,
    averageSlippage: metrics.average_slippage,
  };
}

/**
 * Fetch the main dashboard snapshot in one sequence.
 *
 * @param {QuantyzeClient} client - Quantyze API client.
 * @returns {Promise<Object>} Combined UI snapshot.
 */
async function fetchDashboardSnapshot(client) {
  const [bookSummary, metrics] = await Promise.all([
    client.bookSummary(),
    client.metrics(),
  ]);
  return buildDashboardSnapshot(bookSummary, metrics);
}

if (typeof window !== "undefined") {
  window.QuantyzeUI = {
    QuantyzeClient,
    buildDashboardSnapshot,
    fetchDashboardSnapshot,
  };
}
