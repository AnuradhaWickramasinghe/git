package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class AddressMatchingTest {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://www.openreach.co.uk/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testAddressMatching() throws Exception {
    driver.get(baseUrl + "/orpg/home/index.do");
    driver.findElement(By.cssSelector("span.arrow")).click();
    driver.findElement(By.linkText("Login")).click();
    driver.findElement(By.name("USER")).clear();
    driver.findElement(By.name("USER")).sendKeys("testuse");
    driver.findElement(By.name("USER")).clear();
    driver.findElement(By.name("USER")).sendKeys("testuser10@bt.com");
    driver.findElement(By.name("PASSWORD")).clear();
    driver.findElement(By.name("PASSWORD")).sendKeys("pa55w0rd");
    driver.findElement(By.cssSelector("input.actionBtn")).click();
    driver.findElement(By.linkText("Address matching")).click();
    driver.findElement(By.linkText("Launch application")).click();
    driver.findElement(By.name("simpleSearchPostcode")).clear();
    driver.findElement(By.name("simpleSearchPostcode")).sendKeys("LE4 0BN");
    driver.findElement(By.name("btnValueSimpleSearch")).click();
    driver.findElement(By.linkText("Gold, 1, Greenlawn Walk, Leicester, Leicestershire,...LE4 0BN")).click();
    driver.findElement(By.linkText("Logout")).click();
    assertEquals("A00029897910", driver.findElement(By.xpath("//*[@id=\"T_F2\"]/form/fieldset/div[1]/div/div[1]/span[2]")).getText());
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
