package myapp;

import java.lang.Math;
import java.io.IOException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class DemoServlet extends HttpServlet {
  private static final long serialVersionUID = -5314714338427418156L;
  int MAX_NUMBER = 1000000;

  @Override
  public void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws IOException {
    resp.setContentType("text/html");
    resp.getWriter().println(randomNumberGenerator());
  }
  private int randomNumberGenerator() {
    return (int) Math.floor((Math.random() * MAX_NUMBER) + 1);
  }
}
