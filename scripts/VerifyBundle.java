import java.io.*;
import java.nio.file.*;
import java.security.cert.*;
import java.util.*;
import java.util.jar.*;

/** Verify every bundle payload entry, using the expected upload certificate. */
public class VerifyBundle {
  public static void main(String[] args) throws Exception {
    byte[] expected = Files.readAllBytes(Path.of(args[1]));
    int verified = 0;
    try (JarFile jar = new JarFile(args[0], true)) {
      var entries = jar.entries();
      byte[] buffer = new byte[65536];
      while (entries.hasMoreElements()) {
        JarEntry entry = entries.nextElement();
        if (entry.isDirectory() || entry.getName().startsWith("META-INF/")) continue;
        try (InputStream in = jar.getInputStream(entry)) {
          while (in.read(buffer) != -1) { }
        }
        var certs = entry.getCertificates();
        if (certs == null || Arrays.stream(certs).noneMatch(c -> {
          try { return Arrays.equals(expected, c.getEncoded()); }
          catch (CertificateEncodingException e) { throw new RuntimeException(e); }
        })) throw new SecurityException("Unsigned or unexpected signer: " + entry.getName());
        verified++;
      }
    }
    if (verified == 0) throw new SecurityException("Empty bundle");
    System.out.println("AAB: " + verified + " payload entries verified against upload certificate.");
  }
}
